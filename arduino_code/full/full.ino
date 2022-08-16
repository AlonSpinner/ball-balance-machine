// Touch screen library with X Y and Z (pressure) readings as well
// as oversampling to avoid 'bouncing'
// This demo code returns raw readings, public domain

#include <stdint.h>
#include "TouchScreen.h"
#include <Servo.h>

#define YP A2  // must be an analog pin, use "An" notation!
#define XM A3  // must be an analog pin, use "An" notation!
#define YM 8   // can be a digital pin
#define XP 9   // can be a digital pin

Servo servoA, servoB, servoC;

float x, y; //measurements
float pitch, roll; // controll variables
float Kx = 0.005, Ky = 0.005; // control parameters [rad/mm]
float l0 = 20.0, r = 56.0; //mm
float width = 180, height = 140; //mm
float A, B, C; // motor angles
float motor_min = -20, motor_max = 20; //deg

// For better pressure precision, we need to know the resistance
// between X+ and X- Use any multimeter to read it
// For the one we're using, its 300 ohms across the X plate
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

void setup(void) {
  Serial.begin(9600);
  servoA.attach(2);
  servoB.attach(3);
  servoC.attach(4);
}

float mymap(float x, float fromLow, float fromHigh, float toLow, float toHigh) {
  x = (x-fromLow) / (fromHigh-fromLow) * (toHigh-toLow) + toLow;
  return x - (toHigh-toLow)/2;
}

float motor_sat(float input) {
  if(input > motor_max) return motor_max;
  else if (input < motor_min) return motor_min;
  else return input;
}

float rad2deg (float rad) {
  return rad * 180.0/3.1415;
}

void loop(void) {
  TSPoint p = ts.getPoint();
  if (p.z > ts.pressureThreshhold) {
 
      x = mymap((float)p.x, 70.0 ,960.0, 0.0, width); //measurements
      y = mymap((float)p.y, 116.0, 930.0, 0.0, height);
    
      pitch = y * Ky;
      roll = x * Kx;
    
      A = motor_sat(rad2deg(1.154 * r *tan(pitch)/l0));
      B = motor_sat(rad2deg(-0.577 * r * tan(roll)/l0));
      C = -B;
      
     Serial.print("X = "); Serial.print(x);
     Serial.print("\tY = "); Serial.print(y);
     Serial.println();

     Serial.print("\tpitch = "); Serial.print(rad2deg(pitch));
     Serial.print("\troll = "); Serial.print(rad2deg(roll));
     Serial.println();

     Serial.print("\tA = "); Serial.print(A);
     Serial.print("\tB = "); Serial.print(B);
     Serial.print("\tB = "); Serial.print(C);
     Serial.println();
  }
  else {

   A = motor_min;
   B = motor_min;
   C = motor_min;
  }

  servoA.write(A);
  servoB.write(B);  
  servoC.write(C);  

  delay(50);
}
