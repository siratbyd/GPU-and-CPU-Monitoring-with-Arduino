import wmi
import serial
import time

ser = serial.Serial('COM3', 115200) #set your baudrate and using port as same as on Ardunio IDE


while True:
    w = wmi.WMI(namespace="root\OpenHardwareMonitor")
    temperature_infos = w.Sensor()
    #You can modify the code to get different values stored in OpenHardwareMonitor.
    for sensor in temperature_infos:
        if sensor.SensorType==u'Temperature':
            if sensor.Name==u'GPU Core': #We are searching "GPU Core" heat here, also we can search "GPU Hotspot" or like these values.
                namee = print("GPU")
                ser.write("GPU:".encode())
                temp = print(sensor.Value)
                ser.write(str(sensor.Value).encode())
            elif sensor.Name==u"CPU Package": #As same as like "GPU Core" we are searhing "CPU Package".
                namee = print("CPU")
                ser.write("CPU:".encode())
                temp = print(sensor.Value)
                ser.write(str(sensor.Value).encode())
            else:
                continue #We need to use "continue" here, otherwise the code will show us the other temperature values in OpenHardwarMonitor.
    time.sleep(5)
