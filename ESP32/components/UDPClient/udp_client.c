/* BSD Socket API Example

   This example code is in the Public Domain (or CC0 licensed, at your option.)

   Unless required by applicable law or agreed to in writing, this
   software is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
   CONDITIONS OF ANY KIND, either express or implied.
*/
#include <string.h>
#include <sys/param.h>
#include <sys/types.h>
#include <sys/socket.h>
#include "freertos/FreeRTOS.h"
#include "freertos/task.h"
#include "freertos/event_groups.h"
#include "esp_system.h"
#include "esp_event.h"
#include "esp_log.h"
#include "lwip/err.h"
#include "lwip/sockets.h"
#include "lwip/sys.h"
#include <lwip/netdb.h>
#include "packets.h"
#include "sensors.h"
#if defined(CONFIG_EXAMPLE_IPV4)
#define HOST_IP_ADDR CONFIG_EXAMPLE_IPV4_ADDR
#elif defined(CONFIG_EXAMPLE_IPV6)
#define HOST_IP_ADDR CONFIG_EXAMPLE_IPV6_ADDR
#else
#define HOST_IP_ADDR ""
#endif

#define PORT 8010

static const char *TAG = "example";

// Receives a destination address and a protocol number and returns the protocol payload size,
//      storing the retrieved data in dest. Pointer should be freed as malloc is used
void get_protocol_payload(char* dest, char protocol, short payload_size){
    
    header(dest,protocol,1,payload_size);
    // Adding battery and time
    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    dest[12] = 1;
    memcpy(&(dest[13]),&batt_time,5);

    // Adding temperature, humidity, co2 and pressure
    if (protocol > 0){
        THCP thcp;
        read_thcp_sensor(&thcp);
        memcpy(&(dest[18]),&thcp,10);
    }

    if (protocol > 1){
        ACC_KPI kpi;
        read_acc_kpi_sensor(&kpi);
        if (protocol == 2) {
            memcpy((void*) (&dest[28]), (void*) (&kpi), 4);
        } else {
            memcpy((void*) (&dest[28]), (void*) (&kpi), 28);
        }   

    }

}


void udp_client_task(char protocol,void *pvParameters){
    char rx_buffer[2];
    int addr_family = 0;
    int ip_protocol = 0;

    while (1) {

#if defined(CONFIG_EXAMPLE_IPV4)
        struct sockaddr_in dest_addr;
        dest_addr.sin_addr.s_addr = inet_addr(HOST_IP_ADDR);
        dest_addr.sin_family = AF_INET;
        dest_addr.sin_port = htons(PORT);
        addr_family = AF_INET;
        ip_protocol = IPPROTO_IP;
#elif defined(CONFIG_EXAMPLE_IPV6)
        struct sockaddr_in6 dest_addr = { 0 };
        inet6_aton(HOST_IP_ADDR, &dest_addr.sin6_addr);
        dest_addr.sin6_family = AF_INET6;
        dest_addr.sin6_port = htons(PORT);
        dest_addr.sin6_scope_id = esp_netif_get_netif_impl_index(EXAMPLE_INTERFACE);
        addr_family = AF_INET6;
        ip_protocol = IPPROTO_IPV6;
#endif

        int sock = socket(addr_family, SOCK_DGRAM, ip_protocol);
        if (sock < 0) {
            ESP_LOGE(TAG, "Unable to create socket: errno %d", errno);
            break;
        }

        // Set timeout of reception to 10 secs 
        struct timeval timeout;
        timeout.tv_sec = 10;
        timeout.tv_usec = 0;
        setsockopt (sock, SOL_SOCKET, SO_RCVTIMEO, &timeout, sizeof timeout);

        ESP_LOGI(TAG, "Socket created, sending to %s:%d", HOST_IP_ADDR, PORT);

        // Socket creado

        char layer = 1; 
        short payload_size;
        switch(protocol){
            case 0:
                payload_size = 18;
                break;
            case 1:
                payload_size = 28;
                break;
            case 2:
                payload_size = 32;
                break;
            case 3:
                payload_size = 56;
                break;
            default:
                payload_size = -1;
                break;
        }
        char* payload = malloc(payload_size);
        get_protocol_payload(payload,protocol, payload_size);
        struct sockaddr_storage source_addr; // Large enough for both IPv4 or IPv6
        socklen_t socklen = sizeof(source_addr);
        
        while (layer) {            
            // Send data
            int sent = sendto(sock, payload,payload_size,0,(struct sockaddr *)&source_addr, socklen);
            if (sent < 0){
                ESP_LOGE(TAG, "Error ocurred during sending: errno %d", errno);
                break; 
            }
            // Wait for a response 
            int len = recvfrom(sock, rx_buffer, sizeof(rx_buffer) - 1, 0, (struct sockaddr *)&source_addr, &socklen);
            if (len > 0){
                // Received an answer. Assume layer change
                layer = 0;                 
            } else {
                if (errno != ETIMEDOUT){
                    ESP_LOGE(TAG, "Recv failed, errno = %d", errno);
                    break; 
                }
            }
            vTaskDelay(2000 / portTICK_PERIOD_MS);
        }
        free(payload);
        if (sock != -1) {
            ESP_LOGE(TAG, "Shutting down socket and restarting...");
            shutdown(sock, 0);
            close(sock);
        }
    vTaskDelete(NULL);
    }
}
