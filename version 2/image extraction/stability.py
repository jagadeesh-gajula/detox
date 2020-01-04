import psutil
x=[p.name().lower() for p in psutil.process_iter()]
print(x)