#include <LiquidCrystal.h>

// Initialize the LCD with the pins it's connected to
LiquidCrystal lcd(8, 9, 4, 5, 6, 7);

void setup() {
  // Set the baud rate for serial communication
  Serial.begin(115200);

  // Initialize the LCD
  lcd.begin(16, 2);
  lcd.clear();
}

void loop() {
  if(Serial.available()){
    String namee = Serial.readString();
    lcd.home();
    lcd.print(namee);
    lcd.setCursor(2, 0);
    String temp = Serial.readString();
    lcd.print(temp);
    lcd.setCursor(2, 1);
  }
}
