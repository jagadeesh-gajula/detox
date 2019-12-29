import os
stream = os.popen('tasklist')
output = stream.read()
print(output)
