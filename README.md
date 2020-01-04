# t-wristband-micropython

## Flash MicroPython firmware first:
* ./macOS/esptool --chip esp32 --port /dev/cu.SLAB_USBtoUART erase_flash

* ./macOS/esptool --chip esp32 --port /dev/cu.SLAB_USBtoUART write_flash -z 0x1000 esp32-idf4-20200104-v1.12-35-g10709846f.bin 



## Use ampy to upload py files:

* ampy -p /dev/cu.SLAB_USBtoUART put ST7735.py 

* ampy -p /dev/cu.SLAB_USBtoUART run boot.py 

## TODO:

* fix screen offset
* MPU9250 etc..
