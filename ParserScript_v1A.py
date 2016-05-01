# Miguel
#
# Copyright (C) 2016 Tai Sun and Miguel Lopez
# Contact:
#      t25sun@uwaterloo.ca
#      melopezn@uwaterloo.ca
#
# $GCODEPARSER_BEGIN_LICENSE:MIT$
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# $GCODEPARSER_END_LICENSE$
'''
  * This script reads the Gcode File
  * sends the commands to the arduino
'''
import fileinput
import serial
import time
import sys
import math
ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
counter = 32

"""while (True):
	counter += 1
	print str(chr(counter))
	ser.write(str(chr(counter)))
	#print ser.readline()
	time.sleep(1)
	#sys.exit()"""

units = 'units'
cmd = ''
val = 0
CONST_MOVE = 255
CONST_X_AXIS = 254
CONST_Y_AXIS = 253
CONST_Z_AXIS = 252

def send_Split_int( length ):
    ## check how many integers are going to be sebt
    if ( length - ( length // 200 ) ) == 0:
        ser.write(str(chr(length//200)))
    else:
        ser.write(str(chr( (length//200) + 1)))
    ## send fractioned integer
    amountToSend = 200
    amountRemaining = length
    while math.fabs(amountRemaining) > 0:
        if math.fabs(amountRemaining) >= 200:
            amountToSend = amountRemaining
            amountRemaining = 0
        else:
            amountToSend = 200
            amountRemaining = amountRemaining - amountToSend
        ser.write(str(chr(amountToSend)))
        time.sleep(.1)

def G1(lengthList, units, cmds = [], *args):
    print(' Move '),
    ser.write(str(chr(CONST_MOVE)))
    for index in range(1, lengthList, 2):
        if (cmds[index] == 'X'):
            ser.write(str(chr(CONST_X_AXIS)))
            print (' in X direction: '),
            print (cmds[index + 1] + ' %s' %(units)),
            send_Split_int(int(float(cmds[index + 1])))
            time.sleep(0.1)
        elif (cmds[index] == 'Y'):
            ser.write(str(chr(CONST_Y_AXIS)))
            print (' in Y direction: '),
            print (cmds[index + 1] + ' %s' %(units)),
            send_Split_int(int(float(cmds[index + 1])))
            time.sleep(0.1)
        elif (cmds[index] == 'F'):
            ##ser.write('F')
            print (' with speed: '),
            print (cmds[index + 1] + ' %s/sec' %(units)),
            send_Split_int(int(float(cmds[index + 1])))
            time.sleep(0.1)
    print ('')


def main():
    time.sleep(5)
    for line in fileinput.input(['rect.txt']):
        array = line.split()
        lengthList = len(array)
        if lengthList > 0:
            if array[0] == 'G1':
                G1(lengthList, units, array)

if __name__ == '__main__':
    main()

## 255 -> move command
## 254 -> x axis
## 253 -> y axis
## 252 -> z axis
