import datetime
import os
import pyautogui as pe
import time
import pyperclip
import socket


pe.hotkey('win', 'r'), time.sleep(1), pe.typewrite('cmd'), time.sleep(1), pe.press('enter')
time.sleep(1), pe.typewrite('ping google.com'), pe.press('enter'), time.sleep(9)
pe.hotkey('ctrl', 'a'), pe.hotkey('ctrl', 'c'), pe.hotkey('Alt', 'F4')

s = pyperclip.paste()
date = datetime.date.today()
with open('temp.txt', 'w') as g:
    g.write(s)

f = open('temp.txt', 'r')
lines = f.readlines()
try:
    socket.create_connection(('Google.com', 80))
    if os.path.exists('Final Message') is True:
        with open('Final Message.txt', 'a') as w:
            w.write("\n \nYour ping is %s" % lines[28], )
            w.write("\nWith the packet loss of %s" % lines[24])
            w.write("\n")
            w.write(str(date))
            w.write('\n \n')
            w.write('-' * 100)
    elif os.path.exists('Final Message') is False:
        with open('Final Message.txt', 'w') as w:
            w.write("\nYour ping is %s" % lines[28], )
            w.write("\nWith the packet loss of %s\n" % lines[24])
            w.write("\n")
            w.write(str(date))
            w.write('\n \n')
            w.write('-' * 100)
except OSError:
    with open('Final Message.txt', 'a') as w:
        w.write("\n You seem to be having a network issue. Please try again later")
        w.write("\n")
        w.write(str(date))
        w.write('\n \n')
        w.write('-' * 100)

f.close()
os.remove('temp.txt')
time.sleep(1)
os.startfile('Final Message.txt')
