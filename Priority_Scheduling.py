from collections import defaultdict , deque
from sys import stdin , stdout
import math , heapq
listin = lambda: list(map(int,input().split()))
mapin = lambda: map(int,input().split())

def getWaitTime(process,n,wt):
    wt[0] = 0
    for i in range(1,n):
        wt[i] = process[i-1][1] + wt[i-1]

def getTAT(process,n,wt,tat):
    for i in range(n):
        tat[i] = process[i][1] + wt[i]

def getAvgTime(process,n):
    wt , tat , ct = [0]*n , [0]*n , 0
    getWaitTime(process,n,wt)
    getTAT(process,n,wt,tat)
    print()
    print('Processes ' + '  Burst-Time '+ '  Completion-Time ' + '   Wait-Time ' + '    TurnAroundTime')
    total_wt = 0
    total_tat = 0
    for i in range(n): 
        total_wt += wt[i]  
        total_tat += tat[i] 
        print(" ", str(process[i][0]) + "\t\t" + 
                   str(process[i][1]) + "\t\t" + 
                   str(tat[i]) + '\t\t' + 
                   str(wt[i]) +  "\t\t " + str(tat[i]))

    print('Average TAT = ' + str(round(total_tat/n,2)))
    print('Average WT = ' + str(round(total_wt/n,2)))

def priority_order(process,n):
    process = sorted(process,key = lambda process : process[2],reverse = True)
    print('Priority Order of processes: ')
    for link in process:
        print(link[0],end= ' ')
    getAvgTime(process,n)


if __name__ == "__main__":
    n = int(input("Enter number of process: "))
    process_k = [[0 for i in range(3)] for j in range(n)]
    process = []
    print('Enter the process-ID,Burst-Time,Priority followed by space ')
    for i in range(n):
        id , bt , prio_num = map(int,input().split())
        process.append([id,bt,prio_num])
    priority_order(process,n)