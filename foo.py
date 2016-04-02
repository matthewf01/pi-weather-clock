import time

def foo():
 while(True):
  print ("foo")
  time.sleep(2)
  
def bar():
 while(True):
  print ("bar")
  time.sleep(2)
  
 while(True):
  foo()
  bar()
