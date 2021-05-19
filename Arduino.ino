int LED = 13; // define LED Interface
int Shock = 3; // define the percussion Sensor Interface
int val; // define numeric variables val

void setup()
{
  pinMode (LED, OUTPUT) ; // define LED as output interface
  //pinMode (Shock,INPUT) ; // define knock sensor output inferface
  Serial.begin(9600);
  }
 void loop()
{
  delay(5000);
  val = analogRead(Shock); // read digital interface is assigned a value of 3 val
  Serial.println(val);
  if (val == HIGH) // When the percussion when the sensor detects a signal, LED flashes
  {
    digitalWrite (LED, LOW);
  }
  else
  {
    digitalWrite (LED, HIGH);
  }
}
