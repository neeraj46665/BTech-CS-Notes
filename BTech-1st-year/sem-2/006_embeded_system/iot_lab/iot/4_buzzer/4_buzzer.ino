int buzzer=9;
void setup() {
  // put your setup code here, to run once:
  pinMode(buzzer,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0;i<=25;i=i+5){
    analogWrite(buzzer,i);
    delay(1000);
  }
  for(int i=255;i>=0;i=i-5){
    analogWrite(buzzer,i);
    delay(1000);
  }
}
