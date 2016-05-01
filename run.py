#Miguel
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
** THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
** "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
** LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
** A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
** OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
** SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
** LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
** DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
** THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
** (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
** OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
**
** $GCODEPARSER_END_LICENSE$
**
****************************************************************************/
'''
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
