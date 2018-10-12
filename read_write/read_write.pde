import controlP5.*;
import processing.serial.*;

Serial portA, portB;
ControlP5 cp5;

int recData;
char stateA, stateB;

char switchState(char state){
  if(state == 'L'){
    state = '\n';
  }else{
    state = 'L';
  }
  return state;
}

void setup(){
  size(256, 256);
  portA = new Serial(this, "/dev/cu.usbmodem14111", 115200);
  portB = new Serial(this, "/dev/cu.usbmodem14141", 115200);
  cp5 = new ControlP5(this);
  ControlFont cf = new ControlFont(createFont("Arial", 12));
  cp5.addButton("buttonA")
     .setLabel("A")
     .setPosition(50, 50)
     .setSize(60, 30)
     .setFont(cf)
     .setColorBackground(color(255, 0, 0));
  cp5.addButton("buttonB")
     .setLabel("B")
     .setPosition(120, 50)
     .setSize(60, 30)
     .setFont(cf)
     .setColorBackground(color(0, 0, 255));  
}

void draw(){
  background(0);
}

void buttonA(){
  println("buttonA clicked");
  stateA = switchState(stateA);
  portA.write(stateA);
}

void buttonB(){
  println("buttonB clicked");
  stateB = switchState(stateB);
  portB.write(stateB);
}

void serialEvent(Serial p){
  if(p.available() > 0){
    if(p == portA){
      recData = portA.read();
      print("portA : " + recData + "\n");
      println(recData);
    }else if(p == portB){
      recData = portB.read();
      print("portB : " + recData + "\n");
    }
  }
}
