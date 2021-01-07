import serial


def start_COM(port):
    ser = serial.Serial(port, 115200, timeout=1)
    print('Port name: ' + ser.name)
    data = []
    file = open('../data/new_data.csv', 'w')

    data.append(ser.readlines())
    command = 'current'
    byte_command = str.encode(command+'\n\r')
    ser.write(byte_command)
    for i in range(190):
        serialString = ser.readline()
        line = serialString.decode('Ascii')
        a, b = line.split('\n')
        a = a.replace('\t', ';')
        if 'POS' in a:
            a = 'POS;FW;RW;TO;TC\n'
        file.write(a)
    print('Data updated')
    file.close()
    ser.close()


start_COM('COM3')
