from paramiko_client import ParamikoClient
import time
from multiprocessing import Pool

def process(section,task_command):
    client = ParamikoClient('config.ini',section)
    client.Connect()
    client.run_command(task_command)


if __name__ == '__main__':
    pool = Pool()
    pool.apply_async(process,args=('ssh0','ls /tmp'))
    pool.apply_async(process,args=('ssh1','date'))
    pool.close()
    pool.join()
    print('main process end')