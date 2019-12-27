hosts = open('C:\Windows\System32\Drivers\etc\hosts','a+')
hosts.write("\nthis is not any shit")   
hosts.close()
    
hosts=open('C:\Windows\System32\Drivers\etc\hosts','r')
for line in hosts:
    print(line)

hosts.close()
