import psutil 
import os
import time

def kill(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            p = psutil.Process(proc.pid)

            if not 'SYSTEM' in p.username:
                proc.kill()


while True:
    time.sleep(2)
    x=[p.name().lower() for p in psutil.process_iter()]
    if 'cprog.exe' in x:
        if x.count('cprog.exe') > 1:
            kill('cprog.exe')

    if x.count('cprog.exe') > 1:
            kill('cprog.exe')

    else:
        stream=os.popen('cprog')