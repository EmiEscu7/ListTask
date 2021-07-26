import os
import threading
from win10toast import ToastNotifier

def Notifier0():
    os.system('python notifier.py 0')

def Notifier1():
    os.system('python notifier.py 1')

def Notifier6():
    os.system('python notifier.py 6')

def Notifier24():
    os.system('python notifier.py 24')

def gui():
    os.system('python gui.py')

noti0 = threading.Thread(target=Notifier0)
noti1 = threading.Thread(target=Notifier1)
noti6 = threading.Thread(target=Notifier6)
noti24 = threading.Thread(target=Notifier24)
gui = threading.Thread(target=gui)
noti0.start()
noti1.start()
noti6.start()
noti24.start()
gui.start()