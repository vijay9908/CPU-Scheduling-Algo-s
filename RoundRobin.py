from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def getWaitTime(process,n,bt,wt,slice_time):
    global_time = 0
    balance_bt = [0 for i in range(n)]
    for i in range(n):
        balance_bt[i] = bt[i] 
    while(True):
        res = True
        for i in range(n):
            if balance_bt[i] > 0:
                res= False
                if balance_bt[i] > slice_time:
                    global_time += slice_time
                    balance_bt[i] -= slice_time
                else:
                    global_time += balance_bt[i]
                    wt[i] = global_time - bt[i]
                    balance_bt[i] = 0
        if res == True:
            break

def getTAT(process,n,bt,wt,tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def getAvgTime(process,n,bt,slice):
    wt , tat , comptime = [0]*n , [0]*n , [0]*n
    getWaitTime(process,n,bt,wt,slice)
    getTAT(process,n,bt,wt,tat)
    print('Processes ' + '  Burst-Time '+ '  Completion-Time ' + '   Wait-Time ' + '    TurnAroundTime')
    total_wt , total_tat = 0 , 0
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]  
        comptime.append(tat[i])
        print('    ' + str(i+1) + '\t\t' + str(bt[i]) + '\t\t' +
                    str(tat[i]) + '\t\t' +  str(wt[i]) + '\t\t' + str(tat[i]))
    print('Average TAT = ' + str(round(total_tat/n,2)))
    print('Average WT = ' + str(round(total_wt/n,2)))
    
    

if __name__ == "__main__":
    n = int(input('Enter Number of processes: '))
    process = [i for i in range(n)]
    print('Enter the burst times of processes followed by space')
    burst_time = listin()
    slice_time = int(input('Enter Time-Slice in Seconds: '))
    getAvgTime(process,n,burst_time , slice_time)
    