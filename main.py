'''
Installation:
    $ pip3 install serial pyserial minimalmodbus 
'''
import minimalmodbus as mmb
import serial

# Setting up Modbus device parameters
device = mmb.Instrument('/dev/tty.usbserial-A602TMW2', 1)  # Serial port name, Slave ID
device.mode = mmb.MODE_RTU                      # rtu or ascii mode
device.serial.baudrate = 9600                   # Baud rate
device.serial.bytesize = 8                      # Data size
device.serial.parity   = serial.PARITY_EVEN     # Parity bit
device.serial.stopbits = 1                      # Stop bit
device.serial.timeout  = 5                      # Timeout in seconds


'''
Function code definition 
- https://minimalmodbus.readthedocs.io/en/stable/modbusdetails.html?highlight=function%20code#implemented-functions
    
'''
try:
    print("{:25} {:05.2f}".format('Voltage:', device.read_float(0, functioncode=4)))
    print("{:25} {:>6.2f}".format('Current:', device.read_float(6, functioncode=4)))
    print("{:25} {:>6.2f}".format('Power Factor:', device.read_float(30, functioncode=4)))
    print("{:25} {:>6.2f}".format('Frequency:', device.read_float(70, functioncode=4)))
    print("{:25} {:>6.2f}".format('Active Power(W):', device.read_float(12, functioncode=4)))
    print("{:25} {:>6.2f}".format('Apparent Power(VA):', device.read_float(18, functioncode=4)))
    print("{:25} {:>6.2f}".format('Reactive Power(VAr):', device.read_float(24, functioncode=4)))
    print("{:25} {:>6.2f}".format('Import Energy(kWh):', device.read_float(72, functioncode=4)))

    
    # print(device.read_register(28, functioncode=3)) # Read baudrate in float
    # print(device.write_float(28, 3, 2))             # Write 9600 baud
    # print(device.read_register(18, functioncode=3)) # Read parity and stop bits setting
    # print(device.write_float(18, 1, 2))             # Write even parity and one stop bit
    
except IOError:
    print("Failed to read from device")