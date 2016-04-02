import time
import threading
from threading import Thread

def foo():
 while(True):
  print ("foo")
  time.sleep(2)
  
def bar():
 while(True):
  print ("bar")
  time.sleep(2)
  

if __name__ == '__main__':
    Thread(target = foo).start()
    Thread(target = bar).start()
