
#include <Servo.h>

Servo servoA, servoB, servoC;

float mymap(float x, float fromLow, float fromHigh, float toLow, float toHigh) {
  x = (x-fromLow) / (fromHigh-fromLow) * (toHigh-toLow) + toLow;
  return x - (toHigh-toLow)/2;
}

void setup() {
  servoA.attach(9);
  servoB.attach(5);
  servoC.attach(6);
}

void loop() {
  servoA.writeMicroseconds(map(100, 0, 180, 1000, 2000));
  servoB.writeMicroseconds(map(75, 0, 180, 1000, 2000));
  servoC.writeMicroseconds(map(110, 0, 180, 1000, 2000));
  delay(15);
}
