
# -*- coding: utf-8 -*-
import paramiko
 
pkey='/root/.ssh/id_rsa'  #本地密钥文件路径[此文件服务器上~/.ssh/id_rsa可下载到本地]

#key=paramiko.RSAKey.from_private_key_file(pkey,password='******') #有解密密码时,
key=paramiko.RSAKey.from_private_key_file(pkey)

paramiko.util.log_to_file('paramiko.log')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #通过公共方式进行认证 (不需要在known_hosts 文件中存在)

#ssh.load_system_host_keys() #如通过known_hosts 方式进行认证可以用这个,如果known_hosts 文件未定义还需要定义 known_hosts
#ssh.connect('120.92.209.128',username = 'root',password='******',pkey=key) #这里要 pkey passwordkey 密钥文件
ssh.connect('',username = 'root',pkey=key) #这里要 pkey passwordkey 密钥文件

stdin,stdout,stderr=ssh.exec_command('free -m')
print (stdout.read().decode())

