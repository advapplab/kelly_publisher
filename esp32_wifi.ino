#include <WiFi.h>
const int RDIF  = 5;

WiFiClient client;

//const char *ssid     = "P880";   //WIFI名稱 P880 KAILI_WIFI
//const char *password = "107bef416dac";  //密碼 107bef416dac kelly2014
//const char *host = "192.168.1.104"; //server IP //104 PC //102 Phone //kelly 192.168.0.104

const char *ssid     = "KAILI_WIFI";   //WIFI名稱 P880 KAILI_WIFI
const char *password = "kelly2014";  //密碼 107bef416dac kelly2014
const char *host = "192.168.0.104"; //server IP //104 PC //102 Phone //kelly 192.168.0.104

const int tcpPort = 8705;
void setup() {
  // put your setup code here, to run once:
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

void loop() {
  // put your main code here, to run repeatedly:
  int RDIF_state = 0;   
  RDIF_state = digitalRead(RDIF);
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
  if(RDIF_state == LOW)
    {
     client.write('x');
     Serial.print("hvae people");
     delay(1000);
    }

}
