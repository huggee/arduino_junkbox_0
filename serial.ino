#define LED_PIN 2

int recData = 0;

void setup(){
  Serial.begin(115200);
  pinMode(LED_PIN, OUTPUT);
}

void loop(){
  if(recData == 'L'){
    digitalWrite(LED_PIN, HIGH);
  }else{
    digitalWrite(LED_PIN, LOW);
  }
}

void serialEvent(){
  if(Serial.available() > 0){
    recData = Serial.read();
    Serial.write('L');
  }
}
