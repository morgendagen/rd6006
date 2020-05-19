from rd6006 import RD6006
from pymodbus.client.sync import ModbusTcpClient
from pymodbus.transaction import ModbusRtuFramer


client = ModbusTcpClient(host='192.168.111.193', port=23, framer=ModbusRtuFramer)
r = RD6006(client)
r.status()
