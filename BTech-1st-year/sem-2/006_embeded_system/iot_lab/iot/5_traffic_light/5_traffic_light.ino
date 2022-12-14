int red=8;
int yellow=9;
int green=10;
void setup() {
  // put your setup code here, to run once:
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
  pinMode(A1,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
   int temp = analogRead(A1);
 if(temp < 50 && temp >1 )
 {
 digitalWrite(red, HIGH);
 digitalWrite(yellow, LOW);
 digitalWrite(green, LOW);

 }
 else if(temp < 100 && temp >50)
 {
 digitalWrite(red, LOW);
 digitalWrite(yellow, HIGH);
 digitalWrite(green, LOW); 

  }
 else if(temp <150 && temp >100)
 {
 digitalWrite(red, LOW);
 digitalWrite(yellow, LOW);
 digitalWrite(green, HIGH);

 }
}
