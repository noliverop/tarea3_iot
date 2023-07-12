import pygatt
import time
import logging

adapter = pygatt.GATTToolBackend()

uuids = {
    "status": "0000ff01-0000-1000-8000-00805f9b34fb",
    "protocol_id": "0000ff02-0000-1000-8000-00805f9b34fb",
    "acc_samp": "0000ff03-0000-1000-8000-00805f9b34fb",
    "acc_sens": "0000ff04-0000-1000-8000-00805f9b34fb",
    "gyr_sens": "0000ff05-0000-1000-8000-00805f9b34fb",
    "bme_samp": "0000ff06-0000-1000-8000-00805f9b34fb",
    "discontinuous_time": "0000ff07-0000-1000-8000-00805f9b34fb",
    "tcp_port": "0000ff08-0000-1000-8000-00805f9b34fb",
    "udp_port": "0000ff09-0000-1000-8000-00805f9b34fb",
    "host_addr": "0000ff0a-0000-1000-8000-00805f9b34fb",
    "ssid": "0000ff0b-0000-1000-8000-00805f9b34fb",
    "passwd": "0000ff0c-0000-1000-8000-00805f9b34fb",
}


def bt_read_caracts(mac):
    
    
    logging.basicConfig()
    logging.getLogger('pygatt').setLevel(logging.DEBUG)
    qty = 0

    vals = {}

    while(qty<100):
        try:
            print("entro al try")
            
            adapter.start()
            print("paso el start")
            device = adapter.connect(mac, timeout=2.0)
            print('Se conecto!')

            for key in uuids.keys():
                if key not in vals:
                    vals[key] = device.char_read(uuids[key])

        except pygatt.exceptions.NotConnectedError:
            qty += 1
            print("Se han fallado: {qty} intentos" )
            print("Not connected")
            time.sleep(1)
        finally:
            print("entro al finally")
            adapter.stop()

    return vals