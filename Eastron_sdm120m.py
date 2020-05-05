import minimalmodbus as mmb
import serial

class SDM120M(mmb.Instrument):
    def __init__(self, portname, slaveaddress):
        mmb.Instrument.__init__(self, portname, slaveaddress)
        self.mode = mmb.MODE_RTU 

    
    def configure_serial(self, config_list):
        self.serial.baudrate = config_list[0]           # Baud rate
        self.serial.bytesize = config_list[1]           # Data size

        if config_list[2].upper() == 'E':
            self.serial.parity   = serial.PARITY_EVEN   # Even parity bit
        elif config_list[2].upper() == 'O':
            self.serial.parity   = serial.PARITY_ODD    # Odd parity bit
        elif config_list[2].upper() == 'N':
            self.serial.parity   = serial.PARITY_NONE   # No parity bit 
        
        self.serial.stopbits = config_list[3]           # Stop bit
        self.serial.timeout  = config_list[4]           # Timeout in seconds

    def get_voltage(self):
        return self.read_float(0, functioncode=4)

    def get_current(self):
        return self.read_float(6, functioncode=4)

    def get_power_active(self):
        return self.read_float(12, functioncode=4)

    def get_power_apparent(self):
        return self.read_float(18, functioncode=4)
    
    def get_power_reactive(self):
        return self.read_float(24, functioncode=4)

    def get_power_factor(self):
        return self.read_float(30, functioncode=4)

    def get_frequency(self):
        return self.read_float(70, functioncode=4)

    def get_import_power_active(self):
        return self.read_float(72, functioncode=4)

    def get_baudrate(self):
        return self.read_register(28, functioncode=3) # Read baudrate as float

    def set_baudrate(self, baudrate):
        '''
        0 - 2400
        1 - 4800
        2 - 9600
        '''
        return self.write_float(28, baudrate, 2) 

    def get_stop_parity_config(self):
        return self.read_register(18, functioncode=3) # Read parity and stop bits setting

    def set_stop_parity_config(self, config):
        '''
        0 - One stop bit and no parity
        1 - One stop bit and even parity
        2 - One stop bit and odd parity
        3 - Two stop bits and no parity
        '''
        return self.write_float(18, config, 2)