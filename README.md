
# Execution

* Send data to Dashboard

The following is the execution command to report object has been detected on the outout of the equipements. At the following example, we give a parameter `02`, which denoted as the 2nd equipement. Of course `01` denotes as the 1st equipement.

On the other hand, to make sure the connection has been established, every run will first sleep `1` second berfore send data, and `5` seconds after send data, therefore, we added `&` means we recommend the program should run at the background due to the sensor trigger working frequency is larger than 6 seconds.

```sh
$ python3 send_data.py 02 &

```
* How to execute on windows 10

In the repo, you can find `start01.bat`  ~  `start05.bat`. 
The five `.bat` files stand for running number `01`  ~  `05` of the equipements.
At the following example, if we want to start detecting the number `3` of the equipements.
We just execute `start03.bat`

* Machine Port

```
Machine 01 : 8787
Machine 02 : 8702
Machine 03 : 8703
Machine 04 : 8704
Machine 05 : 8705
```
