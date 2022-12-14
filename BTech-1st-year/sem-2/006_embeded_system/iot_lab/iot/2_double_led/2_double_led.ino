int led_red=3;
int led_green=6;
void setup() {
  // put your setup code here, to run once:
  pinMode(led_red,OUTPUT);
  pinMode(led_green,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(led_red,HIGH);
  digitalWrite(led_green,LOW);
  delay(500);
  digitalWrite(led_red,LOW);
  digitalWrite(led_green,HIGH);
  delay(500);

}
