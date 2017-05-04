# coding=utf-8
__author__ = "xuejun"

'''
concurrent.futures 库提供了一个 ProcessPoolExecutor 类，
可被用来在一个单独的Python解释器中执行计算密集型函数。
'''

import gzip
import io
import glob

def find_robots(filename):
    '''
    Find all of the hosts that access robot.txt in a single log file.
    '''
    robots = set()
    with gzip.open(filename) as f:
        for line in io.TextIOWrapper(f, encoding='ascii'):
            fields = line.split()
            if fields[6] == '/robot.txt':
                robots.add(fields[0])

        return robots

def find_all_robots(logdir):
    '''
    Find all hosts across and entire sequence of files.
    '''
    files = glob.glob(logdir+"/*.log.gz")
    all_robots = set()
    for robot in map(find_robots, files):
        all_robots.update(robots)

    return all_robots

def find_all_robots_use_process(logdir):
    '''
    Find all hosts across and entire sequence of files use ProcessPoolExecutor.
    '''
    from concurrent import ProcessPoolExecutor
    files = glob.glob(logdir+"/*.log.gz")
    all_robots = set()
    with ProcessPoolExecutor() as pool:
        for robots in pool.map(find_robots, files):
            all_robots.update(robots)

    return all_robots


if __name__ == '__main__':
    robots = find_all_robots('logs')
    for ipaddr in robots:
        print(ipaddr)
