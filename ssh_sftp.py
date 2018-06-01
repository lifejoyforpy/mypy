import paramiko,os


transport=paramiko.Transport(('192.168.1.104',22))
transport.connect(username='root',password='admin123')
sftp=paramiko.SFTPClient.from_transport(transport)
# 将location.py 上传到服务器 '/temp/test.py'
#print(sys.path)
print(os.stat(r'E:\python\ftp_server\test\笔记'))


sftp.put('E:\\python\\ftp_server\\test\\笔记','/temp/test.py')
# 将remove_path 下载到本地local_path
#sftp.get('remove_path','local_path')
transport.close()