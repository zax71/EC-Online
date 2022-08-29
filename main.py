import network, socket, time, machine, urequests, json
from picozero import pico_temp_sensor, pico_led
from machine import Pin
import displayControler as display
from secrets import secrets

ssid = secrets["WIFI_SSID"]
password = secrets["WIFI_Password"]

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        for i in range(0, 10):
            display.displayNum(i)
            time.sleep(0.1)
        
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def get(IP):
    request = urequests.get(IP)
    
    return json.loads(request.content)

def displayPlayers():
    playerCount = get("http://mcapi.xdefcon.com/server/mc.endercube.net/full/json")["players"]
    display.displayNum(playerCount)
    return playerCount

def getTime():
    dateTime = get("http://worldtimeapi.org/api/timezone/Europe/London")["datetime"]
    time = dateTime[11:13]
    return int(time)
    

# Connect to WIFI
try:
    ip = connect()
except KeyboardInterrupt:
    machine.reset()




display.clearScreen()

# try/except/finally block
try:
    # Main loop
    while True:
        
        # Is it in operating hours?
        if getTime() >= 9 or getTime() <= 21:
            print(str(displayPlayers()))
            time.sleep(5)
        else:
            display.clearScreen()
            print(f"Not executing because the time is {getTime()}h")
            time.sleep(60)

# Exit cleanly
except KeyboardInterrupt:
    display.clearScreen()
finally:
    display.clearScreen()
    





