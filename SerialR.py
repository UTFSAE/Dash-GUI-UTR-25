import serial

class SerialR:
    def __init__(self, port):
        self.ser = serial.Serial('dev/ttyUSB0', 9600)

    def readData(self):
        output = []

        data = self.ser.readline()
        data = data[2:]
        data = data[:-4]

        if data.lower() == "start":
            data = self.ser.readline()
            data = data[2:]
            data = data[:-4]
            output.append(True)
            if data.lower() == "rpm":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)
            if data.lower() == "gear":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)
            if data.lower() == "mph":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)
            if data.lower() == "coolant":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)
            if data.lower() == "voltage":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)
            if data.lower() == "lap":
                data = self.ser.readline()
                data = data[2:]
                data = data[:-4]
                output.append(data)

        return output
