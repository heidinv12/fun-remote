#include <IRremote.h>

int receiverPin = 2;
IRrecv receiver(receiverPin);
decode_results results;

void setup() {
  Serial.begin(9600);
  receiver.enableIRIn();
}

void loop() {
  if(receiver.decode(&results)){
    Serial.println(results.value, HEX);
    receiver.resume();
  }
  delay(600);
}
