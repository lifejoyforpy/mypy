import paramiko,sys

#创建ssh对象
ssh= paramiko.SSHClient()
#允许链接不在know_hosts 里面的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 链接远程服务器
ssh.connect(hostname='192.168.1.104',port=22,username='root',password='admin123')

#执行命令
stdin ,stdout,stderr=ssh.exec_command('df')
#获取结果
result=stdout.read().decode()

print(result)
ssh.close()
