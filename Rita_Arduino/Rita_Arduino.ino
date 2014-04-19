/*
 Input Pullup Serial
 
 This example demonstrates the use of pinMode(INPUT_PULLUP). It reads a 
 digital input on pin 2 and prints the results to the serial monitor.
 
 The circuit: 
 * Momentary switch attached from pin 2 to ground 
 * Built-in LED on pin 13
 
 Unlike pinMode(INPUT), there is no pull-down resistor necessary. An internal 
 20K-ohm resistor is pulled to 5V. This configuration causes the input to 
 read HIGH when the switch is open, and LOW when it is closed. 
 
 created 14 March 2012
 by Scott Fitzgerald
 
 http://www.arduino.cc/en/Tutorial/InputPullupSerial
 
 This example code is in the public domain
 
 */
int L = 2;
int R = 4;
int Enter = 7;

void setup(){
  //start serial connection
  Serial.begin(9600);
  //configure pin2 as an input and enable the internal pull-up resistor
  pinMode(L, INPUT_PULLUP);
  pinMode(R, INPUT_PULLUP);
  pinMode(Enter, INPUT_PULLUP);
  pinMode(13, OUTPUT); 

}

void loop(){
  //read the pushbutton value into a variable

  if(digitalRead(L)==0) {
    delay(100);
    while (digitalRead(L)==0) {
      delay(10);
    }
    Serial.println("L"); 
  }
  if(digitalRead(R)==0) {
    delay(100);
    while (digitalRead(R)==0) {
      delay(10);
    }
    Serial.println("R"); 
  }
  if(digitalRead(Enter)==0) {
    delay(100);
    int counter = 100;
    while (digitalRead(Enter)==0) {
      delay(10);
      counter--;
    }
    if (counter<0) {
      Serial.println("D");
      } else {
    Serial.println("E"); 
    }
  }
  //print out the value of the pushbutton


    // Keep in mind the pullup means the pushbutton's
  // logic is inverted. It goes HIGH when it's open,
  // and LOW when it's pressed. Turn on pin 13 when the 
  // button's pressed, and off when it's not:

}

