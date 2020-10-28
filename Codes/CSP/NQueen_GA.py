import random
import math
import numpy as np
from matplotlib import pyplot as plt
class nqueen_csp: 
    def __init__(self, q_num): 
        #q_num: number of queens
        self.size = q_num
    
    def initial_population(self,pop_size):       
        initial_pop = [[random.randrange(self.size) for val in range(self.size)] for pop in range(pop_size) ]
        return initial_pop
    
    def select(self,population): 
        #selects an assignment 
        #here we use tournament selection with pool size 2

        pool_size = 5
        r = random.randrange(len(population))
        s = population[r]
        for i in range(pool_size): 
            r = random.randrange(len(population))
            s1 = population[r]
            if self.eval(s1) < self.eval(s): 
                s = s1
        return s
        
    def crossover(self, parent1, parent2,Pc): 
        if(random.uniform(0,1)<=Pc):
            cross_point = random.randrange(self.size)
            child1 = parent1[:cross_point]+parent2[cross_point:]
            child2 = parent2[:cross_point]+parent1[cross_point:]
            return child1, child2
        else: 
            return parent1, parent2
    
    def mutation(self, assignment, Pm): 
        if(random.uniform(0,1)<=Pm):
            p1 = random.randrange(self.size)
            p2 = random.randrange(self.size)
            temp = assignment[p1]
            assignment[p1] = assignment[p2]
            assignment[p2] = temp




   
    def eval(self,assignment): 
        #count the num of conflicts
        conflict_num = 0        
        #Diagonal check
        for r in range(self.size): 
            for k in range(1,self.size-r):
                if  (assignment[r+k] == assignment[r] or assignment[r+k] == assignment[r]+k) or (assignment[r+k] == assignment[r]-k): 
                    conflict_num = conflict_num + 1
        return conflict_num

    def search(self,pop_size,Pc,Pm,iteration):
        pop = self.initial_population(pop_size)
        best = []
        for i in range(iteration):
            eval = [self.eval(pop[k]) for k in range(pop_size)]
            I1 = eval.index(max(eval))
            print(i)
            p1= self.select(pop)
            p2 = self.select(pop)
            c1,c2 = self.crossover(p1,p2,Pc)
            self.mutation(c1,Pm)
            self.mutation(c2,Pm)
            if self.eval(c1) < self.eval(c2):
                pop[I1] = c1
            else: 
                pop[I1] = c2
            
            #pop[I2] = c2
            #eval = [self.eval(pop[k]) for k in range(pop_size)]
            best.append(min(eval))
        return best

            
        



a = nqueen_csp(8)
#print(a.initial_population(5))
bests = a.search(200,.8,.2,2000)
plt.plot(list(range(2000)),bests)
plt.show()



            
         

