import paramiko


list_hostname = ["",""]
username = 'root'
password = ''

#发送paramiko日志到syslogin.log文件
#paramiko.util.log_to_file('syslogin.log')

#创建一个SSH客户端client对象
ssh = paramiko.SSHClient()

#创建默认的白名单
policy = paramiko.AutoAddPolicy()
#设置白名单
ssh.set_missing_host_key_policy(policy)

for index in range(len(list_hostname)):
   #创建SSH连接
   ssh.connect(hostname=list_hostname[index],username=username,password=password)

   command1 = 'touch /root/a.txt'
   command2= 'echo "hello word" >> /root/a.txt'
   command3 = 'mv /root/a.txt  /root/b.txt'
   command4 = 'echo "ni shi xiao zhu" >> /root/b.txt'

   #调用远程执行命令方法exec_command()
   stdin, stdout, stderr = ssh.exec_command(command1)
   stdin, stdout, stderr = ssh.exec_command(command2)
   stdin, stdout, stderr = ssh.exec_command(command3)
   stdin, stdout, stderr = ssh.exec_command(command4)
   result = stdout.read().decode()
   print(result)

ssh.close()

