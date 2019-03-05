#include <NmeaParser.h>

NmeaParser parser;

unsigned long lastTimeDataSent = 0;

void setup()
{
  Serial.begin(9600);
}

void loop()
{
  if (Serial.available())
  {
    char c = Serial.read();

    if (parser.encode(c))
    {
      for (byte i = 0; i < parser.getTermsCount(); i++)
      {
        Serial.print(parser.getTerm(i));
        Serial.print('\t');
      }

      Serial.println();
    }
  }

  if(millis() - lastTimeDataSent >= 1000) {
    parser.createStatement("CHECK");
    Serial.print(parser.getStatement());
    lastTimeDataSent = millis();
  }
}