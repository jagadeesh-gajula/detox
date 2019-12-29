import threading 
import os 
def admin():
    print("this is admin",os.getpid())  

def normal():
    path=os.getcwd()+"\sample.exe"
    os.startfile(path)
    print(path)


  


t1 = threading.Thread(target=admin) 
t2 = threading.Thread(target=normal) 
  

t1.start() 

t2.start() 
  

t1.join() 

t2.join() 
print("Done!") 