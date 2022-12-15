import os

file = os.open("/dev/spi_drv0",os.O_RDWR)
line = str.encode(str(10|128))
os.write(file,line)
line = str.encode(str(50|128))
os.write(file,line)
line = str.encode(str(20|128))
os.write(file,line)
line = str.encode(str(30|128))
os.write(file,line)

status = os.read(file,16)
print(status.decode())
