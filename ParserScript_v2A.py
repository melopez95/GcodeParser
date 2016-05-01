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
