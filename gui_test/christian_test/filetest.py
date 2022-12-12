import os
import time

file = os.open("/dev/spi_drv0",os.O_RDWR)
line = str.encode(str(10|128))
os.write(file,line)
line = str.encode(str(50|128))
os.write(file,line)
line = str.encode(str(37|128))
os.write(file,line)
line = str.encode(str(25|128))
os.write(file,line)


status = decode(os.read(file,16))
print(status)
