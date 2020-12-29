from multiprocessing import Pool, TimeoutError
import time
import os

def f(x):
    with open(x, 'a+') as file:
        file.write(x)
        time.sleep(5)
        file.write("finished")

if __name__ == '__main__':
    # start 4 worker processes
    with Pool(processes=4) as pool:

        # 看是否阻塞


        # print "[0, 1, 4,..., 81]"

        # evaluate "os.getpid()" asynchronously
        # pool.apply_async(f, ('11',)) # runs in *only* one process
        pool.apply_async(f, ('22',)) # runs in *only* one process
