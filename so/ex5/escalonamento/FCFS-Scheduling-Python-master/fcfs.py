class fcfs:                                 #Using Class as a C-like structure
    def __init__(self,pid,at,bt):
        self.pid = pid
        self.at = at
        self.bt = bt
        self.ct, self.wt, self.tat, self.st = int(), int(), int(), False
    def __str__(self):
        res = str(self.pid)+"\t"+str(self.at)+"\t"+str(self.bt)+"\t"+str(self.ct)+"\t"+str(self.tat)+"\t"+str(self.wt)
        return res
    def __lt__(self,fcfs):
        return self.at < fcfs.at
    
n = int(input("Enter the number of processes: "))
time,l = 0,[]
for i in range(n):
    p = int(input("Enter the process id: "))
    a = int(input("Enter the arrival time: "))
    b = int(input("Enter the burst time: "))
    l.append(fcfs(p,a,b))
l.sort()                                    #OR if __lt__ is not overloaded, l.sort(key=lambda x:x.at)

for x in l:
    if time >= x.at:
        x.ct = time + x.bt
        time += x.bt
        x.tat = x.ct - x.at
        x.wt = x.tat - x.bt
    else:
        while(time != x.at):
            time += 1
        x.ct = time + x.bt
        time += x.bt
        x.tat = x.ct - x.at
        x.wt = x.tat - x.bt

print("PID\tAT\tBT\tCT\tTAT\tWT")
for x in l:
    print(x)
