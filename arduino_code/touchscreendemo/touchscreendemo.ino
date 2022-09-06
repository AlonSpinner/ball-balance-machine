// Touch screen library with X Y and Z (pressure) readings as well
// as oversampling to avoid 'bouncing'
// This demo code returns raw readings, public domain

#include <stdint.h>
#include "TouchScreen.h"

#define YP A0  // must be an analog pin, use "An" notation!
#define YM A1   // can be a digital pin
#define XP A2   // can be a digital pin
#define XM A3  // must be an analog pin, use "An" notation!
float x, y;

// For better pressure precision, we need to know the resistance
// between X+ and X- Use any multimeter to read it
// For the one we're using, its 300 ohms across the X plate
TouchScreen ts = TouchScreen(XP, YP, XM, YM, 300);

void setup(void) {
  Serial.begin(9600);
}

float mymap(float x, float fromLow, float fromHigh, float toLow = 0.0, float toHigh = 1.0) {
  return (x-fromLow) / (fromHigh-fromLow) * (toHigh-toLow) + toLow;
}

void loop(void) {
  // a point object holds x y and z coordinates
  TSPoint p = ts.getPoint();
  
  // we have some minimum pressure we consider 'valid'
  // pressure of 0 means no pressing!
  x = mymap((float)p.x, 70.0 ,960.0);
  y = mymap((float)p.y, 116.0, 930.0);
  
  if (p.z > ts.pressureThreshhold) {
     Serial.print("X = "); Serial.print(x);
     Serial.print("\tY = "); Serial.print(y);
     Serial.print("\tPressure = "); Serial.println(p.z);
  }

  delay(50);
}
