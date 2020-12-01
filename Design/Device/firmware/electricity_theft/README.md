# Firmware for Electricity Theft

	The firmware that runs on the ESP8266 device

## Setup

This firmware was developed using the ESP Integrated Development Framework (IDF) and runs on the ESP8266 MCU. 

ESP IDF version 4.2 has been used.

The ESP8266 is a MCU with Wi-Fi module onboard. It is a low-cost Wi-Fi microchip, with a full TCP/IP stack and microcontroller capability, produced by Espressif Systems in Shanghai, China. 



## Bill of Coponents

The major components used are listed below;
- i-Snail-VC-100 Phidgets 100Amp AC Current Sensor 
![isnail](../../../../isnail.jpg)
- ESP8266 Nodemcu v3 Wi-Fi Microcontroller
![esp8266](https://cdn.antratek.nl/media/product/5d4/nodemcu-v2-lua-based-esp8266-development-kit-113990105-42d.jpg)
- 3.3VDC 2A power supply
- Others are discrete components like capacitors, diodes, resistors, transistors, etc.

## Configure the project

1. Get the ESP IDF development toolchain from [here]()
1. cd into this parent directory and run
	```
	idf.py menuconfig
	```

	* Set serial port under Serial Flasher Options.

	* Set WiFi SSID and WiFi Password and Maximum retry under Example Configuration Options.

## Build and Flash

Build the project and flash it to the board, then run monitor tool to view serial output:

```
idf.py -p PORT flash monitor
```

(To exit the serial monitor, type ``ctrl-c``.)

See the Getting Started Guide for full steps to configure and use ESP-IDF to build projects.

## Example Output
Note that the output, in particular the order of the output, may vary depending on the environment.

Console output if station connects to AP successfully:
```
I (589) wifi station: ESP_WIFI_MODE_STA
I (599) wifi: wifi driver task: 3ffc08b4, prio:23, stack:3584, core=0
I (599) system_api: Base MAC address is not set, read default base MAC address from BLK0 of EFUSE
I (599) system_api: Base MAC address is not set, read default base MAC address from BLK0 of EFUSE
I (629) wifi: wifi firmware version: 2d94f02
I (629) wifi: config NVS flash: enabled
I (629) wifi: config nano formating: disabled
I (629) wifi: Init dynamic tx buffer num: 32
I (629) wifi: Init data frame dynamic rx buffer num: 32
I (639) wifi: Init management frame dynamic rx buffer num: 32
I (639) wifi: Init management short buffer num: 32
I (649) wifi: Init static rx buffer size: 1600
I (649) wifi: Init static rx buffer num: 10
I (659) wifi: Init dynamic rx buffer num: 32
I (759) phy: phy_version: 4180, cb3948e, Sep 12 2019, 16:39:13, 0, 0
I (769) wifi: mode : sta (30:ae:a4:d9:bc:c4)
I (769) wifi station: wifi_init_sta finished.
I (889) wifi: new:<6,0>, old:<1,0>, ap:<255,255>, sta:<6,0>, prof:1
I (889) wifi: state: init -> auth (b0)
I (899) wifi: state: auth -> assoc (0)
I (909) wifi: state: assoc -> run (10)
I (939) wifi: connected with #!/bin/test, aid = 1, channel 6, BW20, bssid = ac:9e:17:7e:31:40
I (939) wifi: security type: 3, phy: bgn, rssi: -68
I (949) wifi: pm start, type: 1

I (1029) wifi: AP's beacon interval = 102400 us, DTIM period = 3
I (2089) esp_netif_handlers: sta ip: 192.168.77.89, mask: 255.255.255.0, gw: 192.168.77.1
I (2089) wifi station: got ip:192.168.77.89
I (2089) wifi station: connected to ap SSID:myssid password:mypassword
```

