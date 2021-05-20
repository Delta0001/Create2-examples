import serial
import time

# Open a serial connection to Roomba
ser = serial.Serial(port='COM4', baudrate=115200)
# ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)

# Assuming the robot is awake, start safe mode so we can hack.
ser.write(bytes([131]))
time.sleep(.1)

# Write to 7-segment
ser.write(bytes([164, 68, 99, 76, 84]))

# Vader theme
# ser.write(bytes([140, 0, 9, 69, 40, 69, 40, 69, 40, 65, 30, 72, 10, 69, 40, 65, 30, 72, 10, 69, 80])) 

# Play the song we just programmed.
# ser.write(bytes([141, 0]))
# time.sleep(5) # wait for the song to complete, sum([40, 40, 40, 30, 10, 40, 30, 10, 80] = 320 / 64 = 5 sec

# drive
# ser.write(bytes([137, 0, 56, 1, 244]))
# time.sleep(5)

# turn left
ser.write(bytes([137, 0, 255, 0, 1]))
time.sleep(1.7) # roughly 180 degrees
# turn right
ser.write(bytes([137, 0, 255, 255, 255]))
time.sleep(1.7) # roughly 180 degrees

# drive direct
# ser.write(bytes([145, 0, 255, 0, 255]))
# time.sleep(1.5)

# Leave the Roomba in passive mode; this allows it to keep
#  running Roomba behaviors while we wait for more commands.
ser.write(bytes([128]))

# Close the serial port; we're done for now.
ser.close()