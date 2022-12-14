int buzzer=11;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(buzzer,OUTPUT);
  
}

void loop() {
  // put your main code here, to run repeatedly:
  int LDR=analogRead(A0);
  //delay(500);
  Serial.println(LDR);
  if(LDR>512){
    digitalWrite(buzzer,HIGH);
    //delay(10);
    }
  else{
    digitalWrite(buzzer,LOW); 
  }
  delay(500);
}
