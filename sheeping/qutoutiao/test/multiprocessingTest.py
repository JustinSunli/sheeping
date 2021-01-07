# coding: utf-8
from multiprocessing import Pool

import os, time, random
def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
 
if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        time.sleep(10)
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
    
# import multiprocessing
# import time
# 
# def func(msg):
#     print(multiprocessing.current_process().name + '-' + msg)
# 
# if __name__ == "__main__":
#     pool = multiprocessing.Pool(processes=4) # 创建4个进程
#     for i in range(10):
#         msg = "hello %d" %(i)
#         pool.apply_async(func, (msg, ))
#     pool.close() # 关闭进程池，表示不能在往进程池中添加进程
#     pool.join() # 等待进程池中的所有进程执行完毕，必须在close()之后调用
#     print("Sub-process(es) done.")
    