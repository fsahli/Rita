
import processing.serial.*;
Serial myPort;    // The serial port:
String inString;  // Input string from serial port:
int lf = 10;      // ASCII linefeed
String input[];
PFont f;
int ASCII_i=65;
int ASCII_f=90;

int current_char = ASCII_f;
String words="";

void setup() {
    println(Serial.list());
  // I know that the first port in the serial list on my mac
  // is always my  Keyspan adaptor, so I open Serial.list()[0].
  // Open whatever port is the one you're using.
  myPort = new Serial(this, Serial.list()[6], 9600);
  myPort.bufferUntil(lf);
  size(800, 600);
  background(0);

  // Create the font
  //println(PFont.list());
  f = createFont("Georgia", 100);
  textFont(f);
  textAlign(CENTER, CENTER);
} 

void draw() {
  background(0);
  textAlign(CENTER, CENTER);
  // Set the left and top margin
  int margin = 10;
  //translate(margin*4, margin*4);

  int gap = 100;
      for (int i=-2;i<=2;i++) {  
        int display_char=current_char+i;
        if (display_char<ASCII_i) {
          display_char= ASCII_f-(ASCII_i-display_char)+1;
        }
        if (display_char>ASCII_f) {
          display_char= ASCII_i-(ASCII_f-display_char)-1;
        }
        
    char letter = char(display_char);
      
      textSize(50);
      if (i==0) {
        fill(255, 204, 0);
        textSize(100);
      } 
      else {
        fill(255);
      }

     
      text(letter, width/2+i*gap, height/4);

      } 
      textAlign(CENTER, TOP);
      textSize(100);
      text(words, margin, height/2,width-margin,height-margin);
}

void keyPressed() {
    if (keyCode == RIGHT) {
      current_char++;
      if (current_char>ASCII_f) {
          current_char= ASCII_i-(ASCII_f-current_char)-1;
        }
    } else if (keyCode == LEFT) {
      current_char--;
      if (current_char<ASCII_i) {
          current_char= ASCII_f-(ASCII_i-current_char)+1;
        }
    } else if (keyCode == ENTER) {
     print(current_char);
     words+=char(current_char); 
    }
  
}

void serialEvent(Serial p) {
  inString = (myPort.readString());
  char instruction = inString.charAt(0);
      if (instruction == 'R') {
      current_char++;
      if (current_char>ASCII_f) {
          current_char= ASCII_i-(ASCII_f-current_char)-1;
        }
    } else if (instruction == 'L') {
      current_char--;
      if (current_char<ASCII_i) {
          current_char= ASCII_f-(ASCII_i-current_char)+1;
        }
    } else if (instruction == 'E') {
     print(current_char);
     words+=char(current_char); 
    } else if (instruction == 'D') {
     print(current_char);
     words="";
    }
  
}

