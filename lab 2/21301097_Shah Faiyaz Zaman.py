import random

def Genetic_Algorithm_test(capital,historical_prices,population,generation):
    def generate_population(population):
        output=[]
        for i in population:
            string=''
            for k,v in i.items():
                if v<10:
                    string+='0'
                    string+=str(v)
                else:
                    string+=str(v)    
            output.append(string)
        return output
    def fitness_check(capital,historical_prices,chromosome):
        og_capital=capital
        stop_loss=-int(chromosome[0:2])
        take_profit=int(chromosome[2:4])
        trade_size_perct=int(chromosome[4:6])
        init_trade_size=round(capital*(trade_size_perct/100),2)
        for i in range (len(historical_prices)):
            if historical_prices[i]<stop_loss:
                profit_loss_multiplier=stop_loss/100
                profit_loss=round(init_trade_size*profit_loss_multiplier,2)
                capital+=profit_loss
                init_trade_size=capital*(trade_size_perct/100)
            elif historical_prices[i]>take_profit:
                profit_loss_multiplier=take_profit/100
                profit_loss=round(init_trade_size*profit_loss_multiplier,2)
                capital+=profit_loss
                init_trade_size=capital*(trade_size_perct/100)    
            else:
                profit_loss_multiplier=historical_prices[i]/100
                profit_loss=round(init_trade_size*profit_loss_multiplier,2)
                capital+=profit_loss
                init_trade_size=capital*(trade_size_perct/100)
        
        return round(capital-og_capital,2)
    def elitist_returner(population):
        return sorted(population,key=lambda chromo: fitness_check(capital, historical_prices, chromo), reverse=True)
    def crossover(parent1,parent2):
        random_point=random.randrange(0,4,1)
        child1=parent1[0:random_point+1]+parent2[random_point+1:]
        child2=parent2[0:random_point+1]+parent1[random_point+1:]
        return child1,child2
    def mutation_chance():
        chance=round(random.uniform(0, 1), 2)
        if chance<=0.05:
            return True
        else:
            return False
    def mutation(child):
        random_point=random.randrange(0,6,1)
 
        original_value=child[random_point]

        while True:
            new_value=str(random.randrange(0,10,1))
            if new_value!=original_value:
                break
        child=list(child)
        child[random_point]=new_value
        string=''
        for i in child:
            string+=i
        return string   
    best_every_gen=[]
    initial_population=generate_population(population)
 
    for i in range(generation):
       
        elitism=elitist_returner(initial_population)
        best_parent=elitism[0]
        sub_fit1=elitism[1]
        sub_fit2=elitism[2]
        c1,c2=crossover(best_parent,sub_fit1)
        c3,c4=crossover(best_parent,sub_fit2)
        mutation_chance_c1=mutation_chance()
        mutation_chance_c2=mutation_chance()
        mutation_chance_c3=mutation_chance()
        mutation_chance_c4=mutation_chance()
        
        if mutation_chance_c1:
            c1=mutation(c1)
        if mutation_chance_c2:
            c2=mutation(c2)
        if mutation_chance_c3:
            c3=mutation(c3)
        if mutation_chance_c4:
            c4=mutation(c4)
        initial_population=[c1,c2,c3,c4]
        best_from_current_gen=elitist_returner(initial_population)[0]
        best_every_gen.append(best_from_current_gen)  
    # print(elitist_returner(best_every_gen))
    best=elitist_returner(best_every_gen)[0]
    print('Best Strategy: ',{'stop_loss':int(best[:2]),'take_profit':int(best[2:4]), 'trade_size':int(best[4:6])})
    print('Final Profit:',fitness_check(capital,historical_prices,best))
    
     
    
def double_point(population):
    def generate_population(population):
        output=[]
        for i in population:
            string=''
            for k,v in i.items():
                if v<10:
                    string+='0'
                    string+=str(v)
                else:
                    string+=str(v)    
            output.append(string)
        return output
    initial_population=generate_population(population)
    random_parent=(random.sample(initial_population,2))
    random_point_start=random.randrange(0,4,1)
    while True:

        random_point_end=random.randrange(random_point_start+1,6,1)
        
        if random_point_start+2<=random_point_end:
            break
    print('Parents :',random_parent)  
    print('1st and 2nd points: ', random_point_start, random_point_end)  
    return random_parent[0][:random_point_start+1]+random_parent[1][random_point_start+1:random_point_end]+random_parent[0][random_point_end:],random_parent[1][:random_point_start+1]+random_parent[0][random_point_start+1:random_point_end]+random_parent[1][random_point_end:]   
   

    
    



Genetic_Algorithm_test(1000, [-1.2,  3.4,  -0.8,  2.1,  -2.5,  1.7,  -0.3,  5.8,  -1.1,  3.5],[  
{"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)}, {"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), 
"trade_size": random.randrange(1,100,1)},  
{"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)},  
{"stop_loss":random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)} ],10)


c1,c2=(double_point([{"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)}, {"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), 
"trade_size": random.randrange(1,100,1)},  
{"stop_loss": random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)},  
{"stop_loss":random.randrange(1,100,1), "take_profit": random.randrange(1,100,1), "trade_size": random.randrange(1,100,1)} ]))
print('First child: ', c1)
print('Second child: ', c2)