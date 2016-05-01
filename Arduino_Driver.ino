#include <AccelStepper.h>
#include <Wire.h>
#include <Adafruit_MotorShield.h>
#include "utility/Adafruit_MS_PWMServoDriver.h"

const int steps = 5;
const int stepspeed = 800.0;
const int accel = 1000.0;

Adafruit_MotorShield AFMSbot(0x61); // Rightmost jumper closed
Adafruit_MotorShield AFMStop(0x60); // Default address, no jumpers

// Connect two steppers with 200 steps per revolution (1.8 degree)
// to the top shield
Adafruit_StepperMotor *myStepper1 = AFMStop.getStepper(200, 1);
Adafruit_StepperMotor *myStepper2 = AFMStop.getStepper(200, 2);

// you can change these to DOUBLE or INTERLEAVE or MICROSTEP!
// wrappers for the first motor!
void forwardstep1() {
  myStepper1->onestep(FORWARD, SINGLE);
}
void backwardstep1() {
  myStepper1->onestep(BACKWARD, SINGLE);
}
// wrappers for the second motor!
void forwardstep2() {
  myStepper2->onestep(FORWARD, DOUBLE);
}
void backwardstep2() {
  myStepper2->onestep(BACKWARD, DOUBLE);
}

// Now we'll wrap the 3 steppers in an AccelStepper object
AccelStepper stepper1(forwardstep1, backwardstep1);
AccelStepper stepper2(forwardstep2, backwardstep2);

void stepper1F() {
  Serial.println("Stepper1 +");
  stepper1.setMaxSpeed(stepspeed);
  stepper1.setAcceleration(accel);
  stepper1.moveTo(steps);
  stepper1.setCurrentPosition(0);
  stepper1.runToNewPosition(stepper1.targetPosition());
}

void stepper1B() {
  Serial.println("Stepper1 -");
  stepper1.setMaxSpeed(stepspeed);
  stepper1.setAcceleration(accel);
  stepper1.moveTo(-steps);
  stepper1.setCurrentPosition(0);
  stepper1.runToNewPosition(stepper1.targetPosition());
}

void stepper2F() {
  Serial.println("Stepper1 +");
  stepper2.setMaxSpeed(stepspeed);
  stepper2.setAcceleration(accel);
  stepper2.moveTo(steps);
  stepper2.setCurrentPosition(0);
  stepper2.runToNewPosition(stepper2.targetPosition());
}

void stepper2B() {
  Serial.println("Stepper1 -");
  stepper2.setMaxSpeed(stepspeed);
  stepper2.setAcceleration(accel);
  stepper2.moveTo(-steps);
  stepper2.setCurrentPosition(0);
  stepper2.runToNewPosition(stepper2.targetPosition());
}

void setup()
{
  AFMSbot.begin(); // Start the bottom shield
  AFMStop.begin(); // Start the top shield

  Serial.begin(9600);
}

void loop()
{
  //  Serial.println(stepp1er1.targetPosition());
  //  stepper1.setCurrentPosition(0);
  if (Serial.available() > 0 ) {
    int a = Serial.read();
    Serial.println(Serial.read());
    if ( a == 49 ) {
      stepper1F();
    }
    if ( a == 50 ) {
      stepper1B();
    }
    if ( a == 52 ) {
      stepper2F();
    }
    if ( a == 53 ) {
      stepper2B();
    }
  }
}

