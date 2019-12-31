import psutil
import os
def kill(PROCNAME):
    for proc in psutil.process_iter():
        if proc.name == PROCNAME:
            p = psutil.Process(proc.pid)

            if not 'SYSTEM' in p.username:
                proc.kill()




while True:
	x=[p.name().lower() for p in psutil.process_iter()]
	if 'python.exe' not in x:
		stream=os.popen('python thanos.py')

	if x.count('python.exe')>1:
		kill('python.exe')

	else:
		pass