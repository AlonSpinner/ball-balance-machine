// Touch screen library with X Y and Z (pressure) readings as well
// as oversampling to avoid 'bouncing'
// This demo code returns raw readings, public domain

#include <stdint.h>
#include "TouchScreen.h"
#include <Servo.h>

#define YP A0  // must be an analog pin, use "An" notation!
#define YM A1   // can be a digital pin
#define XP A2   // can be a digital pin
#define XM A3  // must be an analog pin, use "An" notation!

Servo servoA, servoB, servoC;

float x, y; //measurements
float pitch, roll; // controll variables
float Kx = 0.005, Ky = 0.005; // control parameters [rad/mm]
float l0 = 20.0, r = 56.0; //mm
float width = 180, height = 140; //mm
float A, B, C; // motor angles
float motor_min = -30, motor_max = 30; //deg
int counter = 0;
int  bias_A = 100;
int  bias_B = 75;
int  bias_C = 110;
bool homing = true;

// For better pressure precision, we need to know the resistance
// between X+ and X- Use any multimeter to read it
// For the one we're using, its 300 ohms across the X plate
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

void setup(void) {
  Serial.begin(9600);
  servoA.attach(9);
  servoB.attach(5);
  servoC.attach(6);
}

void print2serial(void) {
     Serial.print("X = "); Serial.print(x);
     Serial.print("\tY = "); Serial.print(y);
     Serial.println();

     Serial.print("\tpitch = "); Serial.print(rad2deg(pitch));
     Serial.print("\troll = "); Serial.print(rad2deg(roll));
     Serial.println();

     Serial.print("\tA = "); Serial.print((int)A);
     Serial.print("\tB = "); Serial.print((int)B);
     Serial.print("\tC = "); Serial.print((int)C);
     Serial.println();

     Serial.print("\tcounter = "); Serial.print(counter);
     Serial.println();
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

  // check if new point accuired
  if (p.z > ts.pressureThreshhold) {
      x = mymap((float)p.x, 70.0 ,960.0, 0.0, width); //measurements
      y = mymap((float)p.y, 116.0, 930.0, 0.0, height);
      counter = 0;
      homing = false;
  }

  if (counter < 100 && homing == false) {
      counter++;
   
      pitch = y * Ky;
      roll = x * Kx;
    
      A = motor_sat(rad2deg(1.154 * r *tan(pitch)));
      B = motor_sat(rad2deg(-0.577 * r * tan(roll)));
      C = -B;
  }
  else {
      if (homing == false) {
        A = motor_min;
        B = motor_min;
        C = motor_min;
      }

      counter = 0;
      homing = true;
  }

   if (p.z > ts.pressureThreshhold) {
      print2serial();
  }

  servoA.writeMicroseconds(map((int)A + bias_A, 0, 180, 1000, 2000));
  servoB.writeMicroseconds(map((int)B + bias_B, 0, 180, 1000, 2000));
  servoC.writeMicroseconds(map((int)C + bias_C, 0, 180, 1000, 2000));

  delay(15);
}
