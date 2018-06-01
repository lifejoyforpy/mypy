import paramiko,sys


# 基于公钥私钥
"""
如果A想访问B,则在a机器生成rsa的一对密钥，把公钥部分放在要访问的B机器.ssh里。则不用每次都需要密码，直接根据·密钥匹配
"""

#创建ssh对象
ssh= paramiko.SSHClient()
privatekey=paramiko.RSAKey.from_private_key_file('E:\\python\\ftp_server\\test\\id_rsa31.txt')
#允许链接不在know_hosts 里面的主机

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 链接远程服务器
try:
    ssh.connect(hostname='192.168.1.104',port=22, username='root', pkey=privatekey)
except paramiko.ssh_exception.AuthenticationException as e:
    print (e)
#执行命令
stdin ,stdout,stderr=ssh.exec_command('df')
#获取结果
result=stdout.read().decode()

print(result)
ssh.close()


"""
在centos设置时候一定要去修改sshd_config ,
编辑sshd_config，将RSAAuthentication和PubkeyAuthentication两行前面的 # 去掉 
没有选项就添加。
在.ssh文件里把公钥重命名改为authorized_keys  
修改权限，只有用户本身有rw，chmod 600 authorized_keys
"""