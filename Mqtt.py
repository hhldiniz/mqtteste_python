import paho.mqtt.client as mqtt


def on_connect(self, userdata, flags_dict, result):
    print("Conectado\n" + str(result))
    print(str(flags_dict) + "\n")
    client.subscribe("android/light")
    client.subscribe("android/temperature")


def on_message(client, userdata, msg):
    print(str(client)+"\n")
    print(msg.topic + " " + str(msg.payload))


def on_log(self, userdata, level, buf):
    print(buf)


def on_disconnect():
    print("Desconectado!\n")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_log = on_log
client.username_pw_set("esykibhj", "Db37fQWizlO4")
client.on_disconnect = on_disconnect
client.connect("m10.cloudmqtt.com", 14603, 60)
client.loop_forever()
