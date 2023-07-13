idf_component_register(SRCS "tcp_client_v4.c"
                    INCLUDE_DIRS "include"
                    PRIV_REQUIRES packets sensors log esp_system esp_netif esp_hw_support)