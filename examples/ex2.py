import time

from rd6006 import RD6006
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer


client = ModbusTcpClient(host='192.168.111.193', port=23, framer=ModbusRtuFramer)
r = RD6006(client)

print("Set voltage to 1.8V and enable output")
r.voltage = 1.8
r.enable = True
time.sleep(1)

print("Set voltage to 5V and disable output")
r.voltage = 5.0
r.enable = False

time.sleep(1)
r.status()
