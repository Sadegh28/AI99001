import random
import math
from matplotlib import pyplot as plt
class nqueen_csp: 
    def __init__(self, q_num): 
        #q_num: number of queens
        self.size = q_num
    
    def initial_assignment(self): 
        assignment = [random.randrange(self.size) for i in range(self.size) ]
        return assignment

    def next_assignment(self,assignment): 
        next = assignment.copy()
        i = random.randrange(self.size)
        next[i] = random.randrange(self.size)
        return next
    
    def eval(self,assignment): 
        #count the num of conflicts
        conflict_num = 0        
        #Diagonal check
        for r in range(self.size): 
            for k in range(1,self.size-r):
                if  (assignment[r+k] == assignment[r] or assignment[r+k] == assignment[r]+k) or (assignment[r+k] == assignment[r]-k): 
                    conflict_num = conflict_num + 1
        return conflict_num

    def search(self,T,t):
        #T: initial temp
        # t: schedule 
        current = self.initial_assignment()
        step = 0
        steps = []
        evals = []
        while(T > 0): 
            print(T)
            steps.append(step)
            step += 1
            #print(self.eval(current))
            next = self.next_assignment(current)
            delta = self.eval(current) - self.eval(next)
            if delta>0: 
                current = next
            else: 
                #print([T,delta,delta/T])
                p = math.e**((delta)/T)
                #p = math.exp(delta/T)
                #print("p",p)
                r = random.uniform(0,1)
                #print("r",r)
                if(r <= p): 
                    current = next
            print(self.eval(current))
            evals.append(self.eval(current))
            T = T-t
        plt.plot(steps,evals)
        plt.show()
        print(self.eval(current))
        return current



a = nqueen_csp(30)
print(a.search(2.0,0.00005))

            
         

