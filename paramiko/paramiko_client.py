# coding:utf8
# created at 2018/6/26.

import paramiko
import configparser

class ParamikoClient(object):
    def __init__(self,init_file,section):
        self.config = configparser.ConfigParser()
        self.config.read(init_file)
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.sftp_client = None
        self.client_state = 0
        self.section = section

    def Connect(self):
        try:
            self.client.connect(hostname=self.config.get(self.section,'host'),port=self.config.getint(self.section,'port'),username=self.config.get(self.section,'user'),password=self.config.get(self.section,'pwd'),timeout=self.config.getfloat(self.section,'timeout'))
            self.client_state = 1
            return True
        except Exception as e:
            print('except:',e)

    def run_command(self,cmd_str):
        stdin,stdout,stderr = self.client.exec_command(cmd_str)
        for line in stdout:
            print(line)


    def get_sftp_client(self):
        if self.client_state == 0:
            self.Connect()
        if not self.sftp_client:
            self.sftp_client = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client

def get_callback(size1,size2):
    print(size1,size2)
