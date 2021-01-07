import serial

ser = serial.Serial('COM3', 115200, timeout=2)
print(ser.name)
data = []
while True:
    data.append(ser.readlines())
    if not data == [[]]:
        print(data)
    # further processing
    # send the data somewhere else etc
print(data)
ser.close()
