import Eastron_sdm120m as sdm120m


meter = sdm120m.SDM120M('/dev/tty.usbserial-A602TMW2', 1)

meter.configure_serial([9600, 8, 'E', 1, 5])

'''
Function code definition 
- https://minimalmodbus.readthedocs.io/en/stable/modbusdetails.html?highlight=function%20code#implemented-functions
    
'''
try:
    print("{:25} {:05.2f}".format('Voltage:', meter.get_voltage()))
    print("{:25} {:>6.2f}".format('Current:', meter.get_current()))
    print("{:25} {:>6.2f}".format('Power Factor:', meter.get_power_factor()))
    print("{:25} {:>6.2f}".format('Frequency:', meter.get_frequency()))
    print("{:25} {:>6.2f}".format('Active Power(W):', meter.get_power_active()))
    print("{:25} {:>6.2f}".format('Apparent Power(VA):', meter.get_power_apparent()))
    print("{:25} {:>6.2f}".format('Reactive Power(VAr):', meter.get_power_reactive()))
    print("{:25} {:>6.2f}".format('Import Energy(kWh):', meter.get_import_power_active()))
    
except IOError:
    print("Failed to read from device")