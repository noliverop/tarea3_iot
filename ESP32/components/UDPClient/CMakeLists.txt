idf_component_register(SRCS "udp_client.c"
                    INCLUDE_DIRS "include"
                    PRIV_REQUIRES packets sensors log esp_system esp_event)
