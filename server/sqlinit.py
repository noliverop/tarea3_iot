# Data1 = 1
# Data2 = BatteryLevel
# Data3 = Timestamp
# Data4 = Temperature
# Data5 = Pression
# Data6 = Humidity
# Data7 = CO2
# Data8 = AccelerationX
# Data9 = AccelerationY
# Data10 = AccelerationZ

# Llave primaria es la combinacion de ID_DEVICE y TIMESTAMP

create_datos = '''CREATE TABLE Datos (
    ID_DEVICE TEXT NOT NULL,
    MAC TEXT NOT NULL,
    Status INTEGER,
    BatteryLevel INTEGER,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    Temperature FLOAT,
    Pression INTEGER,
    Humidity INTEGER,
    CO FLOAT,
    RMS FLOAT,
    Amp_X FLOAT,
    Frec_X FLOAT,
    Amp_Y FLOAT,
    Frec_Y FLOAT,
    Amp_Z FLOAT,
    Frec_Z FLOAT,
    PRIMARY KEY (ID_DEVICE, MAC, Timestamp)
);'''

# Tabla con los logs de todas las conexiones realizadas
create_logs = '''CREATE TABLE Logs (
    ID_DEVICE INTEGER NOT NULL,
    MAC TEXT NOT NULL,
    TransportLayer INTEGER NOT NULL,
    ID_protocol INTEGER NOT NULL,
    Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP NOT NULL,
    PRIMARY KEY (ID_DEVICE, MAC, Timestamp)
);'''

# Mutable
# Tabla con las configuraciones de conexion de cada dispositivo
# Por mensaje!
create_config = '''CREATE TABLE Config (
        DEVICE_ID INTEGER PRIMARY KEY,
        STATUS INTEGER,
        ID_PROTOCOL INTEGER,
        ACC_SAMPLING INTEGER,
        ACC_SENSIBILITY INTEGER,
        GYRO_SENSIBILITY INTEGER,
        BME688_SAMPLING INTEGER,
        DISCONTINUOUS_TIME INTEGER,
        TCP_PORT INTEGER,
        UDP_PORT INTEGER,
        HOST_ADDR VARCHAR,
        SSID VARCHAR,
        PASS VARCHAR
    );'''

# Tabla con los tiempos de comunicacion y la cantidad de intentos de conexion
create_loss = '''CREATE TABLE Loss (
    ID_DEVICE INTEGER NOT NULL,
    MAC TEXT NOT NULL,
    ConnectionTime DATETIME,
    Attempts INTEGER
);'''

# insertamos la configuracion default
# Protocolo 0, configuracion status 10.
insert_config = '''insert into Config (
        DEVICE_ID,
        STATUS ,
        ID_PROTOCOL ,
        ACC_SAMPLING ,
        ACC_SENSIBILITY ,
        GYRO_SENSIBILITY ,
        BME688_SAMPLING ,
        DISCONTINUOUS_TIME ,
        TCP_PORT ,
        UDP_PORT ,
        HOST_ADDR ,
        SSID ,
        PASS 
    ) values (12612, 0, 30,1,2,3,4,5,6,7,'A','B','C')'''
    
import sqlite3 as sql


conn = sql.connect("DB.sqlite")
cur = conn.cursor()
cur.execute(create_datos)
cur.execute(create_logs)
cur.execute(create_config)
cur.execute(create_loss)
cur.execute(insert_config)
conn.commit()
conn.close()

# inicializa la BDD