import paho.mqtt.client as mqttClient
import time
 
def on_connect(client, userdata, flags, rc):
 
    if rc == 0:
        print("Connected to broker")
        global Connected
        Connected = True
 on 
    else:
 
        print("Connection failed")
 
Connected = False
 
broker_address= "127.0.0.1"
port = 1883
 
client = mqttClient.Client("Nastya")
client.on_connect= on_connect
client.connect(broker_address, port=port)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
 
try:
    direction=1
    value=0
    while True:
 
        if direction == 1:
                value+=1
        else:
                value-=1
        if value == 10 or value == 0:
                direction*=-1
        temp = "temperature,site=room1 value="+str(value)
        print(temp)
        client.publish("sensors",temp)
        time.sleep(2)
 
except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
