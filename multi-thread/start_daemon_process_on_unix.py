#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-06-02
# @Author  : xuejun (xj174850@163.com)
# @Link    : https://github.com/NeuObito

'''
创建一个守护进程的步骤：
首先，一个守护进程必须要从父进程中脱离。因此第一个fork执行之后就立即结束父进程。
在子进程成为孤儿后，立即调用os.setsid()创建了一个全新的会话，并设置子进程成为首领。
一旦守护进程被正确的分离，它会重新初始化标准I/O流指向用户指定的文件。
守护进程的一个通常实践是在一个文件中写入进程ID，可以被其他程序后面使用到。
'''

import os
import sys

import atexit
import signal


def daemonize(pidfile, *, stdin='/dev/null', stdout='/dev/null', stderr='/dev/null'):
    if os.path.exists(pidfile):
        raise RuntimeError('Already running.')

    # First fork (detaches from parent)
    try:
        if os.fork() > 0:
            raise SystemExit(0)  # Parent exit
    except OSError as e:
        raise RuntimeError('fork #1 failed.')

    os.chdir('/')
    os.umask(0)
    os.setsid()

    # Second fork (relnquish session leadership)
    try:
        if os.fork() > 0:
            raise SystemExit(0)
    except OSError as e:
        raise RuntimeError('fork #2 failed.')

    sys.stdout.flush()
    sys.stdout.flush()

    with open(stdin, 'rb', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())

    with open(stdin, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())

    with open(stdin, 'ab', 0) as f:
        os.dup2(f.fileno(), sys.stdin.fileno())

    # write the PID file
    with open(pidfile, 'w') as f:
        print(os.getpid(), file=f)

    # Arrange to have the PID file removed on exit/signal
    atexit.register(lambda: os.remove(pidfile))

    # Signal handler for termination (required)
    def sigterm_handler(signo, frame):
        raise SystemExit(1)

    signal.signal(signal.SIGTERM, sigterm_handler)


def main():
    import time
    sys.stdout.write('Daemon started with pid {}\n'.format(os.getpid()))
    while True:
        sys.stdout.write('Daemon Alive! {}\n'.format(time.ctime()))
        time.sleep(10)


if __name__ == '__main__':
    PIDFILE = '/tmp/daemon.pid'

    if len(sys.argv) != 2:
        print('Usage: {} [start|stop]'.format(sys.argv[0], file=sys.stderr))
        raise SystemExit(0)

    if sys.argv[1] == 'start':
        try:
            daemonize(PIDFILE, stdout='/tmp/daemon.log', stderr='/tmp/daemon.log')
        except RuntimeError as e:
            print(e, file=sys.stderr)
            raise SystemExit(1)

        main()

    elif sys.argv[1] == 'stop':
        if os.path.exists(PIDFILE):
            with open(PIDFILE) as f:
                os.kill(in(f.read()), signal.SIGTERM)
        else:
            print('Not running', file=sys.stderr)
            raise SystemExit(1)

    else:
        print('Unknown command {!r}'.format(sys.argv[1]))
