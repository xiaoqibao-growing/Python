# coding=utf-8

__author__ = "xuejun"

from collections import deque

# Two simple generator functions.
def countdown(n):
    while n > 0:
        print('T-minus:', n)
        yield
        n -= 1

def countup(n):
    x = 0
    while x < n:
        print("Counting up", x)
        yield
        x += 1


class TaskScheduler(object):
    def __init__(self):
        self._task_queue = deque()

    def new_task(self, task):
        '''
        Admit a newly started task to the scheduler.
        '''
        self._task_queue.append(task)

    def run(self):
        '''
        Run until there are no more tasks.
        '''
        while self._task_queue:
            task = self._task_queue.popleft()
            try:
                # Run until the next yield statement
                next(task)
                self._task_queue.append(task)
            except StopIteration:
                pass

# sched = TaskScheduler()
# sched.new_task(countdown(10))
# sched.new_task(countdown(5))
# sched.new_task(countdown(15))
# sched.run()

'''
生成器函数就是认为，而yield语句是任务挂起的信号。
'''
class ActorScheduler(object):
    def __init__(self):
        self._actors = {}
        self._msg_queue = deque()

    def new_actor(self, name, actor):
        self._actors[name] = actor
        self._msg_queue.append((actor, None))

    def send(self, name, msg):
        '''
        Send a message to a named actor.
        '''
        actor = self._actors.get(name)
        if actor:
            self._msg_queue.append((actor, msg))

    def run(self):
        '''
        Run as long as there are pending messages.
        '''
        while self._msg_queue:
            actor, msg = self._msg_queue.popleft()
            print("msg", msg)
            try:
                actor.send(msg)
            except StopIteration:
                pass

if __name__ == '__main__':
    def printer():
        while True:
            msg = yield
            print('GOT:', msg)

    def counter(sched):
        while True:
            # Receive the current count.
            n = yield
            print("n", n)
            if n == 0:
                break
            sched.send("printer", n)
            sched.send("counter", n-1)

    sched = ActorScheduler()
    sched.new_actor('printer', printer())
    sched.new_actor('counter', counter(sched))

    sched.send('counter', 1000)
    sched.run()
