import threading
from time import sleep
import os

a = 1
#线程函数
def music():
    global a
    a = 2
    print(a)
    for i in range(5):
        sleep(2)
        print('喜羊羊与灰太狼',os.getpid())

#创建线程对象
t = threading.Thread(target = music)
t.start()
for i in range(3):
    sleep(3)
    print('舒克和贝塔',os.getpid())
t.join()

print('Main thread a:',a)