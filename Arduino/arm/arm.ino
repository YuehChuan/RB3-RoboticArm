#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

#define MIN_PULSE_WIDTH 800
#define MAX_PULSE_WIDTH 2200
#define DEFAULT_PULSE_WIDTH 1500
#define FREQUENCY 50

uint8_t servonum0 = 0;
int i = 90, j = 30, k = 90;
char a;

void setup() 
{
Serial.begin(115200);
pwm.begin();
pwm.setPWMFreq(FREQUENCY);
pwm.setPWM(2, 0, pulseWidth0(90));
pwm.setPWM(1, 0, pulseWidth0(90));
pwm.setPWM(0, 0, pulseWidth0(i));
pwm.setPWM(3, 0, pulseWidth0(j));
pwm.setPWM(5, 0, pulseWidth0(0));
}
int pulseWidth0(int angle)
{
int pulse_wide, analog_value;
pulse_wide = map(angle, 0, 180, MIN_PULSE_WIDTH, MAX_PULSE_WIDTH);
analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
//Serial.println(analog_value);
return analog_value;
}

int pulseWidth3(int angle)
{
int pulse_wide, analog_value;
pulse_wide = map(angle, 0, 180, 1000, 2000);
analog_value = int(float(pulse_wide) / 1000000 * FREQUENCY * 4096);
//Serial.println(analog_value);
return analog_value;
}

void loop() {
//pwm.setPWM(0, 0, pulseWidth(0));
//Serial.println("AT 0d");
//delay(1500);
//pwm.setPWM(0, 0, pulseWidth(165));
//Serial.println("AT 165d");
//delay(1500);
//pwm.setPWM(0, 0, pulseWidth(90));
//Serial.println("AT 90d");
//delay(5000);

//pwm.setPWM(0, 0, pulseWidth(i));

 if(Serial.available())
 {
  a = Serial.read();

    if (a == 'a' && i != 165)
  {
    pwm.setPWM(0, 0, pulseWidth0(i));
    i++;
    //delay(200);
  }
  else if (a == 'd' && i != 0)
  {
    pwm.setPWM(0, 0, pulseWidth0(i));
    i--;
    //delay(200);
  }
  else if (a == 'w' && j != 165)
  {
    pwm.setPWM(3, 0, pulseWidth0(j));
    j++;
    //delay(200);
  }
   else if (a == 's' && j != 0)
  {
    pwm.setPWM(3, 0, pulseWidth0(j));
    j--;
   // delay(200);
  }

    else if (a == 'r' && k != 160)
  {
    pwm.setPWM(2, 0, pulseWidth0(k));
    pwm.setPWM(1, 0, pulseWidth0(k));
    k++;
    if ( k >= 159 )
    {
      Serial.print('s');
    }

    //delay(100);
  }
   else if (a == 'f' && k != 0)
  {
    pwm.setPWM(2, 0, pulseWidth0(k));
    pwm.setPWM(1, 0, pulseWidth0(k));
    k--;

    //delay(200);
    if ( k <= 80 )
    {
      Serial.print('q');
    }
  }
   else if (a == 'c')
  {
    pwm.setPWM(5, 0, pulseWidth0(165));
  }
   else if (a == 'o')
  {
    pwm.setPWM(5, 0, pulseWidth0(0));
  }

  else if (a == 'm')
  {
    pwm.setPWM(2, 0, pulseWidth0(90));
    pwm.setPWM(1, 0, pulseWidth0(90));
    pwm.setPWM(0, 0, pulseWidth0(90));
    pwm.setPWM(3, 0, pulseWidth0(30));
    pwm.setPWM(5, 0, pulseWidth0(0));
    i = 90;
    j = 30;
    k = 90;
  }

   a = 'k';

 }
 else
  a = 'k';
 




/*
delay(2000);

while( i != 0 )
{
  pwm.setPWM(0, 0, pulseWidth(i));
  i--;
  delay(20);
}

*/
}
