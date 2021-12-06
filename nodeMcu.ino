#include <ESP8266WiFi.h>
#define SensorInput D7
#define RDIF D5

WiFiClient client;



long duration, cm;

//const char *ssid     = "P880";   //WIFI名稱 P880 KAILI_WIFI
//const char *password = "107bef416dac";  //密碼 107bef416dac kelly2014
//const char *host = "192.168.1.104"; //server IP //104 PC //102 Phone //kelly 192.168.0.104

const char *ssid     = "KAILI_WIFI";   //WIFI名稱 P880 KAILI_WIFI
const char *password = "kelly2014";  //密碼 107bef416dac kelly2014
const char *host = "192.168.0.104"; //server IP //104 PC //102 Phone //kelly 192.168.0.104

const int tcpPort = 8787;


    int times = 0;
    int state = 0;
    int RDIF_state = 0;
    boolean switch1 = true;

  void setup()
{

    Serial.begin(9600);    
    pinMode(LED_BUILTIN,OUTPUT);
    //pinMode(SensorInput,INPUT);
    pinMode(RDIF,INPUT);
//    pinMode(trigPin, OUTPUT);        // 定義輸入及輸出 
//    pinMode(echoPin, INPUT);
    
    delay(500);
    Serial.println();
    Serial.print("Connecting to ");
    Serial.println(ssid);

    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) 
    {
        Serial.println("WiFi connection failed......");
        delay(500);
    }

    Serial.println("");
    Serial.println("WiFi connected");
    Serial.println("IP address: ");
    Serial.println(WiFi.localIP());
}
void loop()
{
    state = digitalRead(SensorInput);
    RDIF_state = digitalRead(RDIF);
    Serial.print(state);

    while (!client.connected())   
    {
        if (!client.connect(host, tcpPort))
        {
            Serial.println("connection....");
            delay(500);

        }
        else 
        {
          Serial.println("connect fail");
        }
    }
//    digitalWrite(trigPin, LOW);
//    delayMicroseconds(5);
//    digitalWrite(trigPin, HIGH);     // 給 Trig 高電位，持續 10微秒
//    delayMicroseconds(10);
//    digitalWrite(trigPin, LOW);
//
//    pinMode(echoPin, INPUT);             // 讀取 echo 的電位
//    duration = pulseIn(echoPin, HIGH);   // 收到高電位時的時間

   // cm = (duration/2) / 29.1;

//    Serial.print("Distance : ");  
//    //Serial.print(inches);
//    //Serial.print("in,   ");
//    Serial.print(cm);
      //Serial.print(cm);
      //Serial.println();
//    Serial.print("cm");
//    Serial.println();
//    if(cm <= 30)
//    {
//     client.write('y');
//     state = 0;
//     delay(1000);
//     //delay(500);
//     //Serial.println("Has People");
//     //Serial.println(); 
//    }
    if(RDIF_state == LOW)
    {
     client.write('x');

     delay(1000);
    }
//    if(state!=0)
//    {
//        //times += 1;
//        //byte x = times;
//        //Serial.println();
//        //Serial.println(times);
//      client.write('x');
//      delay(5000);
//    }
//    else if(RDIF_state == HIGH)
//    {
//      //Serial.println("Have People");
//      client.write('y');
//      state = 0;
//      //delay(500);
//      //delay(500);
//    }
    
      
//    client.write(times);
//    while (client.available())
//    {   
//      char val = client.read();
//        if(val=='a'){          
//           digitalWrite(LED_BUILTIN, switch1);
//           if(switch1==true){
//             switch1 = !switch1;
//             client.write("H");
//           }
//           else{
//             switch1 = !switch1;
//             client.write("L");
//           }
//        }
//    }
}
