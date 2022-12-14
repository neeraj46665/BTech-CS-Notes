int red=8;
int yellow=9;
int green=10;
void setup() {
  // put your setup code here, to run once:
  pinMode(red,OUTPUT);
  pinMode(yellow,OUTPUT);
  pinMode(green,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
 digitalWrite(red, HIGH);
 digitalWrite(yellow, LOW);
 digitalWrite(green, LOW);
 delay(500);

 digitalWrite(red, LOW);
 digitalWrite(yellow, HIGH);
 digitalWrite(green, LOW);
 delay(500);

 digitalWrite(red, LOW);
 digitalWrite(yellow, LOW);
 digitalWrite(green, HIGH);
 delay(500);

}
