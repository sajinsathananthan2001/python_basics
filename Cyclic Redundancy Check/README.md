The working of Cyclic redundancy check

![cyclic-redundancy-check](https://github.com/sajinsathananthan2001/c_basic_concepts/assets/93672391/8997bfc4-3858-42e7-a8a0-eca8457edb94)


Let's simplify the Arduino code to send data along with CRC, and we'll adjust the Python code accordingly. We'll use a basic CRC calculation without relying on external libraries for simplicity.

### Arduino Code:

```cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Your data to be sent
  byte sendData[] = {0x01, 0x02, 0x03, 0x04};

  // Calculate CRC for the data
  uint16_t crcValue = calculateCRC(sendData, sizeof(sendData));

  // Send the data along with CRC
  Serial.write(sendData, sizeof(sendData));
  Serial.write((byte*)&crcValue, sizeof(crcValue));

  delay(1000);  // Adjust delay as needed
}

// Basic CRC calculation function
uint16_t calculateCRC(byte data[], size_t length) {
  uint16_t crc = 0xFFFF;
  for (size_t i = 0; i < length; ++i) {
    crc ^= data[i];
    for (size_t j = 0; j < 8; ++j) {
      if (crc & 0x0001) {
        crc = (crc >> 1) ^ 0xA001;  // XOR with CRC-16 polynomial
      } else {
        crc = crc >> 1;
      }
    }
  }
  return crc;
}
```

### Python Code:

```python
import serial
import struct

ser = serial.Serial('COMx', 9600)  # Replace 'COMx' with the appropriate port

def receive_data():
    # Wait until data is available
    while ser.in_waiting == 0:
        pass

    # Receive the data
    received_data = ser.read(4)  # Assuming data size is 4 bytes
    received_crc = ser.read(2)  # Assuming CRC size is 2 bytes

    return received_data, received_crc

def check_crc(data, crc_received):
    # Calculate CRC for the received data
    crc_calculated = calculate_crc(data)

    # Compare calculated CRC with received CRC
    return crc_calculated == struct.unpack('H', crc_received)[0]

def calculate_crc(data):
    crc = 0xFFFF
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x0001:
                crc = (crc >> 1) ^ 0xA001
            else:
                crc = crc >> 1
    return crc

while True:
    data, crc = receive_data()

    if check_crc(data, crc):
        print("CRC Matched!")
        print("Received Data:", data)
    else:
        print("CRC Mismatch! Discarding Data.")
```

#### Explanation:

1. The Arduino code now uses a simple CRC-16 calculation (`calculateCRC` function) to calculate the CRC for the data.
2. The CRC value is sent as a 2-byte value (`uint16_t`).
3. The Python code is adjusted to receive 2 bytes for CRC and calculates the CRC using a similar method.
4. The `check_crc` function compares the calculated CRC with the received CRC.

Make sure to replace 'COMx' with the appropriate COM port on your system in the Python code. Adjust data size and CRC size accordingly based on your specific requirements.