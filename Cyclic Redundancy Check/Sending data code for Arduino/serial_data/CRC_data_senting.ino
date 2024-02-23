#include <CRC32.h>

CRC32 crc;

void setup() {
  Serial.begin(9600);
}

void loop() {
  // Your data to be sent
  byte sendData[] = {0x01, 0x02, 0x03, 0x04};

  // Calculate CRC for the data
  uint32_t crcValue = crc.calculate(sendData, sizeof(sendData));

  // Send the data along with CRC
  Serial.write(sendData, sizeof(sendData));
  Serial.write((byte*)&crcValue, sizeof(crcValue));

  delay(1000);  // Adjust delay as needed
}
