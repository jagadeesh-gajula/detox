import threading 
import os 
def admin():
    print("this is admin",os.getpid())  

def normal():
    print("this is normal",os.getpid())
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=admin) 
    t2 = threading.Thread(target=normal) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 