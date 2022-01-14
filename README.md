
# Execution

* Send data to Dashboard

The following is the execution command to report object has been detected on the outout of the equipements. At the following example, we give a parameter `02`, which denoted as the 2nd equipement. Of course `01` denotes as the 1st equipement.

On the other hand, to make sure the connection has been established, every run will first sleep `1` second berfore send data, and `5` seconds after send data, therefore, we added `&` means we recommend the program should run at the background due to the sensor trigger working frequency is larger than 6 seconds.

```sh
$ python3 send_data.py 02 &

```
* How to execute on windows 10

In the repo, you can find `start01.bat`  ~  `start05.bat`. 
The five `.bat` files stand for running number `01`  ~  `05` of the Equipements.
In the following example, if we want to start detecting the number `3` of the Equipements.
We just execute `start03.bat`

* Machine Port

```
Machine 01 : 8787
Machine 02 : 8702
Machine 03 : 8703
Machine 04 : 8704
Machine 05 : 8705
```

* Machine Number

```
Machine 01 : 01
Machine 02 : 02
Machine 03 : 03
Machine 04 : 04
Machine 05 : 05
```

* Implement Process

```process.bat``` -> ```machine_process.py``` -> ```websocket.py```
* To execute ```process.bat```
```sh
process.bat $PROT $Machine_number 
```
At the following example, to execute `Machine 03`.
```sh
process.bat 8703 03 
```
* Argument

At the following example, `start03.bat`'s content.

```sh
python websocket.py 8703 03 
```
* `8703` is the 1st argument, which denoted as the port of the 3rd Equipement.
* `03` is the 2nd argument, which was the same as the `python send_data.py 03` for sending data.

* Run the send data code in the background on Windows 10 as `&` on Linux
```
START /B python send_data.py 03
```
* Machine Host in the current machine on windows 10 should be static IP address `192.168.0.104`

# Sensor

* Signal Received

In the while loop, you can find ` if recv == 'x':`. It means we received a signal called `'x'` from the sensor when detection.

* Timeout Restart

To prevent the connected error's problem. So when didn't detect over `300` seconds, it will restart the program to reconnect. 
* https://github.com/advapplab/kelly_publisher/blob/main/websocket.py#L75

# Log

* You can find the log on the `01` ~ `05` of the directory.

# Arduino Manual

* [Software Download](https://www.arduino.cc/en/software)

* Board

  [DOIT ESP32 DEVKIT V1](http://www.ho-hua.com.tw/products_data.php?pid=16491)

  [NodeMcu 1.0 (ESP8266)](http://www.ho-hua.com.tw/products_data.php?pid=16490)
  
* Sensor 
  
  [IRS-180](http://www.ho-hua.com.tw/products_data.php?pid=15081)
  
  Output : D5
  
* Files
  
  [esp32_wifi.ino](https://github.com/advapplab/kelly_publisher/blob/main/esp32_wifi.ino)
  
  [nodeMcu.ino](https://github.com/advapplab/kelly_publisher/blob/main/nodeMcu.ino)
  
* Board Libray

  ESP32
  
  https://dl.espressif.com/dl/package_esp32_index.json
  
  NodeMcu (ESP8266)
  
  http://arduino.esp8266.com/stable/package_esp8266com_index.json 
  
  FIle -> Preference -> Additional Boards Manager URLs:
  
  Take the two libray link to add to Additional Boards Manager URLs
  
  ![image](https://github.com/advapplab/kelly_publisher/blob/main/image/0.png)
  
* Boards Manager

  Tools -> Board -> Boards Manager
  
  ![image](https://github.com/advapplab/kelly_publisher/blob/main/image/1.png)
  
  Input the words that `esp32` and `esp8266` at the space separately, and install the libs.
  
  ![image](https://github.com/advapplab/kelly_publisher/blob/main/image/2.png)
  
  ![image](https://github.com/advapplab/kelly_publisher/blob/main/image/3.png)

* Select Board

  Tools -> Board 
  
  Tools -> Port
  
  If you want to use `DOIT ESP32 DEVKIT V1`
  
  From `ESP32 Arudino` to find the board : `DOIT ESP32 DEVKIT V1`
  
  If you want to use `NodeMcu 1.0`
  
  From `ESP8266 Modules` to find the board : `NodeMcu 1.0`
  
* Change TCP PORT
  
  ```
  Machine 01 : 8787
  Machine 02 : 8702
  Machine 03 : 8703
  Machine 04 : 8704
  Machine 05 : 8705
  ```
  ![image](https://github.com/advapplab/kelly_publisher/blob/main/image/4.png)


  
  
  
  
  
 

