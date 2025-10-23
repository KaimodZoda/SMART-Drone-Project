#ifndef DIGIPOT
#define DIGIPOT

#include <SPI.h>
#include "model.h"

extern Eloquent::ML::Port::RandomForest classifier;
extern float flattenedFeatures[];

// Pin definitions for digital potentiometers
#define VRY_CS_PIN 16   // Chip Select pin for VRy (X9C104)
#define VRX_CS_PIN 6   // Chip Select pin for VRx (X9C103S)

// Function prototypes
void setDigitalPotValue(int csPin, int value);
void handleCommand(const String& command);
void moveDrone(float vRyVoltage, float vRxVoltage);
int voltageToStep(float voltage);
void printStatus(const String& action, float vRyVoltage, float vRxVoltage);
void recievecommand();

void digipot_setup() {
  Serial.begin(115200);
  SPI.begin();

  pinMode(VRY_CS_PIN, OUTPUT);
  pinMode(VRX_CS_PIN, OUTPUT);

  // Ensure digital potentiometers are not selected at startup
  digitalWrite(VRY_CS_PIN, HIGH);
  digitalWrite(VRX_CS_PIN, HIGH);

  Serial.println("Drone Controller Initialized");
  Serial.println("Send 'upward', 'hold', or 'downward' to control the drone.");
}
void recievecommand() {
    const char* command = classifier.idxToLabel(classifier.predict(flattenedFeatures));
    handleCommand(command); // Handle the trimmed command
}


void setDigitalPotValue(int csPin, int value) {
  if (value < 0 || value > 255) {
    Serial.println("Error: Value out of range");
    return;
  }

  SPI.beginTransaction(SPISettings(1000000, MSBFIRST, SPI_MODE0));
  digitalWrite(csPin, LOW);
  SPI.transfer(value);
  digitalWrite(csPin, HIGH);
  SPI.endTransaction();
}

void handleCommand(const String& command) {
  if (command == "Up") {
    moveDrone(+3.3, -1.67); // Ascend
    printStatus("Ascending", 5.0, -5.0);
  } else if (command == "Default") {
    moveDrone(+1.25, -1.67); // Hover
    printStatus("Holding Position", 2.5, -2.5);
  } else if (command == "Down") {
    moveDrone(-3.3 , -1.67); // Descend
    printStatus("Descending", 0, 0);
  } else if (command == "Left") {
    moveDrone(1.6, -3.3); // Left
    printStatus("Go Left", 1.6, -3.3);
  } else if (command == "Right") {
    moveDrone(1.6, 0); // Right
    printStatus("Go Left", 1.6, 0);
  } else {
    Serial.println("Error: Invalid command");
  }
}

void moveDrone(float vRyVoltage, float vRxVoltage) {
  setDigitalPotValue(VRY_CS_PIN, voltageToStep(vRyVoltage));
  setDigitalPotValue(VRX_CS_PIN, voltageToStep(vRxVoltage));
}

int voltageToStep(float voltage) {
  // Convert voltage to step value, assuming 5V max and 255 steps
  return round((voltage + 5) / (2 * 4) * 255);
}

void printStatus(const String& action, float vRyVoltage, float vRxVoltage) {
  Serial.print(action);
  Serial.print(" | VRy Voltage: ");
  Serial.print(vRyVoltage);
  Serial.print("V, VRx Voltage: ");
  Serial.print(vRxVoltage);
  Serial.println("V");
}

#endif // DIGIPOT_H