---
title: Interface example
featured_image: incubator-interface.jpg:flux
---

To make sure I understand how a web interface is made via an ESP32, I started with a very basic example. The only thing this minimal example will do is to light on and off the RGB LED connected to the Barduino (ESP32) through the incubator shield I designed via a web interface accessible from any browser (desktop and mobile).

<video><source src="esp-interface-minimal.mp4"></video>
![very very minimal](small:interface-screenshot.png)

## Key elements

### Librairies

Include the librairies: Arduino framework, AnalogWrite to manipulate analog output with the ESP32 and Wifi, the one that interests us here.

<pre>
#include &lt;Arduino.h&gt;
#include &lt;analogWrite.h&gt;
#include &lt;WiFi.h&gt;
</pre>


### Wifi credentials

Include the Wifi network credentials so that the ESP32 can access your wifi.

<pre>
const char *ssid = "********";
const char *password = "********";
WiFiServer server(80);
</pre>

### Initialize the connection

This code is then used to initialize a connection to the address `192.168.1.118`. This IP address is accessible to all devices connected to the same Wifi network.

<pre>
void initWiFi()
{
  Serial.println("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected successfully");
  Serial.print("Got IP: ");
  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("HTTP server started");
  delay(100);
}
</pre>

### Get the header

Information will travel via the URL that we send from one side and receive on the other.
For example, a button will add `/?RED=ON` to the end of our url `192.168.1.118`, forming a `192.168.1.118/?RED=ON` that we can parse to do things in our code.

<pre>
void buildPage()
{
  WiFiClient client = server.available();
  if (client)
  {
    Serial.println("New Client is requesting web page");
    String current_data_line = "";
    while (client.connected())
    {
      if (client.available())
      {
        char new_byte = client.read();
        Serial.write(new_byte);
        header += new_byte;
      }
    }
  }
}
</pre>

### If else conditions

Depending on what we get in the header, we can switch the LED on and off.

<pre>
if (header.indexOf("GET /RED=ON") >= 0)
{
  Serial.println("LED is red");
  active_color = "red";
  rgbLed(100, 0, 0);
}
else if (header.indexOf("GET /?GREEN=ON") != -1)
{
  Serial.println("LED is green");
  active_color = "green";
  rgbLed(0, 100, 0);
}
else if (header.indexOf("GET /?BLUE=ON") != -1)
{
  Serial.println("LED is blue");
  active_color = "blue";
  rgbLed(0, 0, 100);
}
</pre>

### Build the page

To finally build our HTML page with the variables and buttons that allow us to change the colour of the LEDs.

<pre>
client.println("&lt;!DOCTYPE html&gt;&lt;html&lt;");
client.println("&lt;head&gt;&lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"&gt;&lt;/head&gt;");
client.println("&lt;body&gt;&lt;h1&gt;ESP32 minimal example&lt;/h1&gt;");
client.println("&lt;p&gt;The RGB led is currently &lt;b&gt;" + active_color + "&lt;/b&gt;. Click one of the following button to change its color.&lt;/p&gt;");
client.println("&lt;form&gt;");
client.println("&lt;button name=\"RED\" value=\"ON\" type=\"submit\"&gt;RED&lt;/button&gt;");
client.println("&lt;button name=\"GREEN\" value=\"ON\" type=\"submit\"&gt;GREEN&lt;/button&gt;");
client.println("&lt;button name=\"BLUE\" value=\"ON\" type=\"submit\"&gt;BLUE&lt;/button&gt;");
client.println("&lt;/form&gt;");
client.println("&lt;/body&gt;&lt;/html&gt;");
</pre>


## Source code

<pre>
#include &lt;Arduino.h&gt;
#include &lt;analogWrite.h&gt;
#include &lt;WiFi.h&gt;

// Wifi
const char *ssid = "********";
const char *password = "********";
WiFiServer server(80);
String header;

// LED Constants
#define led_red 33
#define led_green 25
#define led_blue 26

// LED Variables
String active_color = "off";

void rgbLed(int red, int green, int blue)
{
  // The values must be reversed because the LED must be pulled down to operate
  analogWrite(led_red, map(red, 0, 255, 255, 0));
  analogWrite(led_green, map(green, 0, 255, 255, 0));
  analogWrite(led_blue, map(blue, 0, 255, 255, 0));
}

void initWiFi()
{
  Serial.println("Connecting to ");
  Serial.println(ssid);
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED)
  {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected successfully");
  Serial.print("Got IP: ");
  Serial.println(WiFi.localIP());
  server.begin();
  Serial.println("HTTP server started");
  delay(100);
}

void buildPage()
{
  WiFiClient client = server.available();
  if (client)
  {
    Serial.println("New Client is requesting web page");
    String current_data_line = "";
    while (client.connected())
    {
      if (client.available())
      {
        char new_byte = client.read();
        Serial.write(new_byte);
        header += new_byte;
        if (new_byte == '\n')
        {
          if (current_data_line.length() == 0)
          {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            if (header.indexOf("GET /RED=ON") >= 0)
            {
              Serial.println("LED is red");
              active_color = "red";
              rgbLed(100, 0, 0);
            }
            else if (header.indexOf("GET /?GREEN=ON") != -1)
            {
              Serial.println("LED is green");
              active_color = "green";
              rgbLed(0, 100, 0);
            }
            else if (header.indexOf("GET /?BLUE=ON") != -1)
            {
              Serial.println("LED is blue");
              active_color = "blue";
              rgbLed(0, 0, 100);
            }
            client.println("&lt;!DOCTYPE html&gt;&lt;html&lt;");
            client.println("&lt;head&gt;&lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1\"&gt;&lt;/head&gt;");
            client.println("&lt;body&gt;&lt;h1&gt;ESP32 minimal example&lt;/h1&gt;");
            client.println("&lt;p&gt;The RGB led is currently &lt;b&gt;" + active_color + "&lt;/b&gt;. Click one of the following button to change its color.&lt;/p&gt;");
            client.println("&lt;form&gt;");
            client.println("&lt;button name=\"RED\" value=\"ON\" type=\"submit\"&gt;RED&lt;/button&gt;");
            client.println("&lt;button name=\"GREEN\" value=\"ON\" type=\"submit\"&gt;GREEN&lt;/button&gt;");
            client.println("&lt;button name=\"BLUE\" value=\"ON\" type=\"submit\"&gt;BLUE&lt;/button&gt;");
            client.println("&lt;/form&gt;");
            client.println("&lt;/body&gt;&lt;/html&gt;");
            client.println();
            break;
          }
          else
          {
            current_data_line = "";
          }
        }
        else if (new_byte != '\r')
        {
          current_data_line += new_byte;
        }
      }
    }
    header = "";
    client.stop();
    Serial.println("Client disconnected.");
  }
}

void setup()
{
  Serial.begin(9600);
  delay(500);
  pinMode(led_red, OUTPUT);
  pinMode(led_green, OUTPUT);
  pinMode(led_blue, OUTPUT);
  rgbLed(0, 0, 0);
  initWiFi();
}

void loop()
{
  buildPage();
}
</pre>