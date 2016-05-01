#Tom
'''
/****************************************************************************
**
** Copyright (C) 2016 Tai Sun and Miguel Lopez
** Contact:
**      t25sun@uwaterloo.ca
**      melopezn@uwaterloo.ca
**
** $GCODEPARSER_BEGIN_LICENSE:MIT$
**
** Permission is hereby granted, free of charge, to any person obtaining a copy
** of this software and associated documentation files (the "Software"), to deal
** in the Software without restriction, including without limitation the rights
** to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
** copies of the Software, and to permit persons to whom the Software is
** furnished to do so, subject to the following conditions:
** 
** The above copyright notice and this permission notice shall be included in all
** copies or substantial portions of the Software.
** 
** THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
** IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
** FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
** AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
** LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
** OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
** SOFTWARE.
**
** $GCODEPARSER_END_LICENSE$
**
****************************************************************************/
'''
'''
  * This script reads the Gcode File
  * sends the commands to the arduino
'''
import time
import fileinput
import serial
import time
import sys

ser = serial.Serial('/dev/ttyUSB0', 9600)

units = 'units'
cmd = ''
val = 0

def serialWrite(dist, dir):
    if dir == 'X':
        if dist[0] == '-':
            dist = dist.replace('-', '')
            for i in range(int(dist)):
                print i
                ser.write(str(2))
                time.sleep(0.07)
        else:
            for i in range(int(dist)):
                print i
                ser.write(str(1))
                time.sleep(0.07)
    elif dir == 'Y':
        if dist[0] == '-':
            dist = dist.replace('-', '')
            for i in range(int(dist)):
                print i
                ser.write(str(5))
                time.sleep(0.07)
        else:
            for i in range(int(dist)):
                print i
                ser.write(str(4))
                time.sleep(0.07)

def G1(lengthList, units, cmds = [], *args):
    for index in range(1, lengthList, 2):
        if (cmds[index] == 'X'):
            serialWrite(cmds[index + 1], 'X')
        elif (cmds[index] == 'Y'):
            serialWrite(cmds[index + 1], 'Y')
        time.sleep(0.5)
    print ('')


def main():
    for line in fileinput.input(['rect.txt']):
        time.sleep(0.5)
        list = line.split()
        if list == 0:
            sys.exit()
        print list
        lengthList = len(list)
        if lengthList == 0:
            sys.exit()
        elif list[0] == 'G1':
            G1(lengthList, units, list)



if __name__ == '__main__':
    main()

'''
while True:
    val = raw_input('Enter value: ')
    for i in range(10):
        ser.write(val)
'''
