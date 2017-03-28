#-*- coding=utf-8 -*-
import time
import random
import multiprocessing
from multiprocessing import Process
from multiprocessing import Pool
import os

import numpy as np


pCOs = np.linspace(1e-5, 0.5, 10)
pO2s = np.linspace(1e-5, 0.5, 10)

def fork_test():
	print("Process (%s) start..." % os.getpid())

	pid = os.fork()  # only work on Unix/Linux/Mac
	if pid == 0:
		print("I am child process (%s) and my parent is %s." % (os.getpid(), os.getpid()))
	else:
		print("I (%s) just created a child process (%s)." % (os.getpid(), pid))


def run_proc(name):
	print("Run child process %s (%s)..." % (name, os.getpid()))


def run_process():
	print("Parent process %s." % os.getpid())
	p = Process(target=run_proc, args=('test',))
	print("Child process will start.")
	p.start()
	p.join()
	print("Child process end.")


def long_time_task(name):
	print("Run task %s (%s)..." % (name, os.getpid()))
	start = time.time()
	time.sleep(random.random()*3)
	end = time.time()

	print("Task %s runs %0.2f seconds." % (name, (end - start)))


def start_pool():
	print("Starting %s." % multiprocessing.current_process().name)

def long_time_task_pool():
	print("Parent process %s." % os.getpid())
	pool_size = multiprocessing.cpu_count() * 2
	p = Pool(processes=pool_size, initializer=start_pool)

	p.map(long_time_task, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
	print("Waiting for all subprocesses done...")
	print("All subprocesses done.")

	p.close()
	p.join()


if __name__ == '__main__':
	long_time_task_pool()
