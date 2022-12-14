int switchh=12;
int motorPos=7;
int motorNeg=6;
void setup(){
    pinMode(switchh,INPUT); 
    pinMode(motorPos,OUTPUT); 
    pinMode(motorNeg,OUTPUT);  
}
void loop(){
    if(digitalRead(switchh)==LOW){
        digitalWrite(motorPos,HIGH);
        digitalWrite(motorNeg,LOW);
//        delay(2000);
      
    } 
    else{
        digitalWrite(motorPos,LOW);
        digitalWrite(motorNeg,LOW);
//        delay(2000);
      
     }
}
