# kelly_publisher

# Execution

The following is the execution command to report object has been detected on the outout of the equipements. At the following example, we give a parameter `02`, which denoted as the 2nd equipement. Of course `01` denotes as the 1st equipement.

On the other hand, to make sure the connection has been established, every run will first sleep `1` second berfore send data, and `5` seconds after send data, therefore, we added `&` means we recommend the program should run at the background due to the sensor trigger working frequency is larger than 6 seconds.

```sh
$ python3 send_data.py 02 &

```