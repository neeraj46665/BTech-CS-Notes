void setup() {
  // put your setup code here, to run once:
  pinMode(13,OUTPUT);
  pinMode(3,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(3)==1){
    digitalWrite(13,LOW);
  }
  else{
    digitalWrite(13,HIGH);
  }
}
