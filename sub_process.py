import subprocess
print('$ nslookup www.baidu.com')
r=subprocess.call(['nslookup','www.baidu.com'])
print('Exit code:',r)
print('==================')
print('$ nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\nwww.baidu.com\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)
