from collections import defaultdict , deque
from sys import stdin , stdout
import math

def getWaitTime(process,n,bt,wt):
    wt[0] = 0 
    for i in range(1,n):
        wt[i] = bt[i-1]+wt[i-1]

def getTurnAroundTime(process,n,bt,wt,tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def getAvgTime(process,n,bt):
    wt , tat = [0 for i in range(n)] , [0 for i in range(n)]
    Total_wt , Total_tat = 0 , 0
    getWaitTime(process,n,bt,wt)
    getTurnAroundTime(process,n,bt,wt,tat)
    comptime = 0
    print('Processes ' + '  Burst-Time '+ '  Completion-Time ' + '   Wait-Time ' + '    TurnAroundTime')
    for i in range(n):
        Total_wt = Total_wt + wt[i]
        Total_tat = Total_tat + tat[i]
        comptime += bt[i]
        print(' ' + str(i+1) + '\t\t' + str(bt[i]) + '\t\t' +
                    str(comptime) + '\t\t' +  str(wt[i]) + '\t\t' + str(tat[i]))
    print('Average WT = ' + str(round(Total_wt/n,2)))
    print('Average TAT = ' + str(round(Total_tat/n,2)))


if __name__ == "__main__":
    n = int(input('Enter Number of processes: '))
    process = [i for i in range(n)]
    print('Enter the burst times of processes followed by space')
    burst_time = list(map(int,input().split()))[:n]
    getAvgTime(process,n,burst_time)

