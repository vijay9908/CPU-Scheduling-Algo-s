from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

class process():
    def __init__(self,burst_time):
        self.bt = burst_time
        self.global_time = 0
        self.priority = 0

class mapDeque():

    def __init__(self,slice_time,priority):
        self.items , self.slice_time , self.priority = [] , slice_time , priority
    
    def addIn(self,item):
        item.global_time = self.slice_time 
        item.priority = self.priority
        self.items.insert(0,item)
    
    def subOut(self):
        return self.items.pop()
    
    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

iter_process = list(mapDeque(i*10,i) for i in range(256))
rem_process = []
current_process = None

def scheduler():
    global current_process
    if current_process is not None:
        index = current_process.priority
        deq = iter_process[index]
        pid = current_process
        if pid.blocking == 1:
            deq.subOut()

            if index == 0:
                iter_process.addIn(pid)
            else:
                iter_process[index-1].addIn(pid)
        elif pid.leave == 1:
            iter_process.subOut()
            rem_process.append({'pid':pid.PID,'Qindex':index})
    else:
        pid.global_time -= 1
        pid.time -= 1
        if pid.global_time <= 0:
            iter_process.subOut()
            if pid.time > 0:
                iter_process[index+1].addIn(pid)
            else:
                pass
        elif pid.time <= 0:
            iter_process.subOut()
        else:
            pass

    for q in enumerate(iter_process):
        if not q.isEmpty():
            current_process = q.peek()
            break
    
def addToQueue(process):
    entry = filter(lambda pp: pp["pid"] == process, rem_process)
    if entry is not None:
        iter_process[entry['Qindex']].addIn(process)
    else:
        iter_process[0].addIn(process)



