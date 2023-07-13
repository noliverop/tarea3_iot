/*
 * SPDX-FileCopyrightText: 2022 Espressif Systems (Shanghai) CO LTD
 *
 * SPDX-License-Identifier: Unlicense OR CC0-1.0
 */
#include "sdkconfig.h"
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <errno.h>
#include <netdb.h>            // struct addrinfo
#include <arpa/inet.h>
#include <sys/time.h>
#include <rtc.h>
#include "esp_netif.h"
#include "esp_log.h"
#include "esp_system.h"
#include "esp_sleep.h"
#include "packets.h"
#include "sensors.h"
#if defined(CONFIG_EXAMPLE_SOCKET_IP_INPUT_STDIN)
#include "addr_from_stdin.h"
#endif

#if defined(CONFIG_EXAMPLE_IPV4)
#define HOST_IP_ADDR CONFIG_EXAMPLE_IPV4_ADDR
#elif defined(CONFIG_EXAMPLE_SOCKET_IP_INPUT_STDIN)
#define HOST_IP_ADDR ""
#endif

#define PORT CONFIG_EXAMPLE_TCP_PORT

static const char *TAG = "example";

// 
void protocolo_0(int sock, char transport_layer){
    char* payload = malloc(18);
    header(payload,0,transport_layer,6);
    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    payload[12] = 1;
    memcpy(&(payload[13]),&batt_time,5);
    int err = send(sock, payload, 18, 0);
    if (err < 0) {
        ESP_LOGE(TAG, "Error occurred during sending: errno %d", errno);
    }
    ESP_LOGI(TAG, "Timestamp: %ld", batt_time.timestamp);
    free(payload);
    return;
}

void protocolo_1(int sock, char transport_layer){
    char* payload = malloc(28);
    header(payload,1,transport_layer,16);
    payload[12] = 1; 
    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    memcpy(&(payload[13]),&batt_time,5);
    THCP thcp;
    read_thcp_sensor(&thcp);
    memcpy(&(payload[18]),&thcp,10);
    int err = send(sock, payload, 28, 0);
    if (err < 0) {
        ESP_LOGE(TAG, "Error occurred during sending: errno %d", errno);
    }
    free(payload);
    return;
}

void protocolo_2(int sock, char transport_layer){
    char* payload = malloc(32);
    header(payload,2,transport_layer,20);
    payload[12] = 1; 

    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    memcpy(&(payload[12]),&batt_time,5);
    
    THCP thcp;
    read_thcp_sensor(&thcp);
    memcpy(&(payload[18]),&thcp,10);
    
    ACC_KPI kpi;
    read_acc_kpi_sensor(&kpi);
    memcpy((void*) (&payload[28]), (void*) (&kpi), 4);
    int err = send(sock, payload, 32, 0);
    if (err < 0) {
        ESP_LOGE(TAG, "Error occurred during sending: errno %d", errno);
    }
    return;
}

void protocolo_3(int sock, char transport_layer){
    char* payload = malloc(56);
    header(payload,3,transport_layer,44);
    payload[12] = 1; 

    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    memcpy(&(payload[13]),&batt_time,5);
    
    THCP thcp;
    read_thcp_sensor(&thcp);
    memcpy(&(payload[18]),&thcp,10);
    
    ACC_KPI kpi;
    read_acc_kpi_sensor(&kpi);
    memcpy((void*) (&payload[28]), (void*) (&kpi), 28);
    int err = send(sock, payload, 56, 0);
    if (err < 0) {
        ESP_LOGE(TAG, "Error occurred during sending: errno %d", errno);
    }
    return;
}

void protocolo_4(int sock, char transport_layer){
    char* payload = malloc(24028);
    header(payload,4,transport_layer,24016);
    payload[12] = 1; 

    BATT_TIME batt_time;
    read_batt_time(&batt_time);
    memcpy(&(payload[13]),&batt_time,5);
    
    THCP thcp;
    read_thcp_sensor(&thcp);
    memcpy(&(payload[18]),&thcp,10);
    
    ACC acc;
    read_accelerometer(&acc);
    int bytes_sent = 0;
    while(bytes_sent<24028){
        int sent = send(sock, payload, 1024, 0);
        if (sent<0){
            ESP_LOGE(TAG, "Error occurred during sending: errno %d", errno);
            break;
        } else {
            bytes_sent += sent; 
        }
    }
    free(acc.acc_x);
    free(acc.acc_y);
    free(acc.acc_z);
    free(payload);
    return;
}

void tcp_client(int sock, char protocol){
    ESP_LOGI(TAG, "ENTERING MAIN FUNCTION");
    char rx_buffer[10];

    ESP_LOGI(TAG,"Protocol: %c, TL: %c", protocol, 0);
    switch (protocol){
        case 0:
            protocolo_0(sock,0);
            break;
        case 1:
            protocolo_1(sock,0);
            break;
        case 2:
            protocolo_2(sock,0);
            break; 
        case 3:
            protocolo_3(sock,0);
            break;      
        case 4:
            protocolo_4(sock,0);
            break;          
        default:
            ESP_LOGE(TAG, "recv failed: errno %d", errno);
    }

    //deep sleep
    int len = recv(sock, rx_buffer, sizeof(rx_buffer) - 1, 0);
    if (len==-1){
        ESP_LOGE(TAG, "Did not receive answer: errno %d", errno);
    }     
    if (sock != -1) {
        ESP_LOGE(TAG, "Shutting down socket and restarting...");
        shutdown(sock, 0);
        close(sock);
    }

    uint64_t sleep_time = (uint64_t) (5*(long long)1e6);
    int ret = esp_sleep_enable_timer_wakeup(sleep_time);
    ESP_LOGI(TAG, "Timer value: %lld ", sleep_time);
    if (ret==ESP_ERR_INVALID_ARG){
        ESP_LOGE(TAG, "Invalid timer value");
    }
    esp_deep_sleep_start();
}