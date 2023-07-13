#include <inttypes.h>

typedef struct {
    int32_t status;
    int32_t protocol;
    int32_t BMI270_Sampling;
    int32_t BMI270_Acc_Sensibility;
    int32_t BMI270_Gyro_Sensibility;
    int32_t BME688_Sampling;
    int32_t Discontinuos_Time; 
    int32_t tcp_port;
    int32_t udp_port; 
    char host_ip_addr[1];
    char ssid[1];
    char pass[1];
} Config;