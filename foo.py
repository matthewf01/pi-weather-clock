import time

def foo():
 while(True):
  print ("foo")
  time.sleep(2)
  
def bar():
 while(True):
  print ("bar")
  time.sleep(2)
  
  
 foo(True)
 bar(True)
