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
	time.sleep(1)
	x=[p.name().lower() for p in psutil.process_iter()]
	print(x.count('nothing.exe'))

	if x.count('nothing.exe') == 0:
		stream=os.popen('nothing.exe')


	if x.count('nothing.exe') > 1:
		kill('nothing.exe')

	else:
		pass