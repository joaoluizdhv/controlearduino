#include <IRremote.h>
 
int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;
 
void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
}

void lerTecla()
{
  int leuTecla = 0;
  int valores;
  while(leuTecla == 0)
  {
    if (irrecv.decode(&results))
    {
      irrecv.resume();
      if(results.value != -1)
      {
        valores = results.value;
        Serial.println(valores);
        leuTecla = 1;
      }
    }
  }
  leuTecla = 0;
  delay(10);
}
 
 
void loop()
{
  lerTecla();
}