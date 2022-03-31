# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 08:43:31 2022
Projet DIA: Tatouine en danger !
.    .        .      .             . .     .        .          .          .
         .                 .                    .                .
  .               A long time ago in a galaxy far, far away...   .
     .               .           .               .        .             .
     .      .            .                 .                                .
 .      .         .         .   . :::::+::::...      .          .         .
     .         .      .    ..::.:::+++++:::+++++:+::.    .     .
                        .:.  ..:+:..+|||+..::|+|+||++|:.             .     .
            .   .    :::....:::::::::++||||O||O#OO|OOO|+|:.    .
.      .      .    .:..:..::+||OO#|#|OOO+|O||####OO###O+:+|+               .
                 .:...:+||O####O##||+|OO|||O#####O#O||OO|++||:     .    .
  .             ..::||+++|+++++|+::|+++++O#O|OO|||+++..:OOOOO|+  .         .
     .   .     +++||++:.:++:..+#|. ::::++|+++||++O##O+:.++|||#O+    .
.           . ++++++++...:+:+:.:+: ::..+|OO++O|########|++++||##+            .
  .       .  :::+++|O+||+::++++:::+:::+++::+|+O###########OO|:+OO       .  .
     .       +:+++|OO+|||O:+:::::.. .||O#OOO||O||#@###@######:+|O|  .
 .          ::+:++|+|O+|||++|++|:::+O#######O######O@############O
          . ++++: .+OO###O++++++|OO++|O#@@@####@##################+         .
      .     ::::::::::::::::::::++|O+..+#|O@@@@#@###O|O#O##@#OO####     .
 .        . :. .:.:. .:.:.: +.::::::::  . +#:#@:#@@@#O||O#O@:###:#| .      .
                           `. .:.:.:.:. . :.:.:%::%%%:::::%::::%:::
.      .                                      `.:.:.:.:   :.:.:.:.  .   .
           .                                                                .
      .
.          .                                                       .   .
                                                                             .
    .        .                                                           .
    .     .                                                           .      .
  .     .                                                        .
              .   A terrible civil war burns throughout the  .        .     .
                 galaxy: a rag-tag group of freedom fighters   .  .
     .       .  has risen from beneath the dark shadow of the            .
.        .     evil monster the Galactic Empire has become.                  .
   .             Imperial  forces  have  instituted  a reign of   .      .
             terror,  and every  weapon in its arsenal has  been
          . turned upon the Rebels  and  their  allies:  tyranny, .   .
   .       oppression, vast fleets, overwhelming armies, and fear.        .  .
.      .  Fear  keeps  the  individual systems in line,  and is the   .
         prime motivator of the New Order.             .
    .      Outnumbered and outgunned,  the Rebellion burns across the   .    .
.      vast reaches of space and a thousand-thousand worlds, with only     .
    . their great courage - and the mystical power known as the Force -
     flaming a fire of hope.                                    .
       This is a  galaxy  of wondrous aliens,  bizarre monsters,  strange   .
 . Droids, powerful weapons, great heroes, and terrible villains.  It is a
  galaxy of fantastic worlds,  magical devices, vast fleets, awesome machi-  .
 nery, terrible conflict, and unending hope.              .         .
.        .          .    .    .            .            .                   .
               .               ..       .       .   .             .
 .      .     T h i s   i s   t h e   g a l a x y   o f   . . .             .
                     .              .       .                    .      .
.        .               .       .     .            .
   .           .        .                     .        .            .
             .               .    .          .              .   .         .
               _________________      ____         __________
 .       .    /                 |    /    \    .  |          \
     .       /    ______   _____| . /      \      |    ___    |     .     .
             \    \    |   |       /   /\   \     |   |___>   |
           .  \    \   |   |      /   /__\   \  . |         _/               .
 .     ________>    |  |   | .   /            \   |   |\    \_______    .
      |            /   |   |    /    ______    \  |   | \           |
      |___________/    |___|   /____/      \____\ |___|  \__________|    .
  .     ____    __  . _____   ____      .  __________   .  _________
       \    \  /  \  /    /  /    \       |          \    /         |      .
        \    \/    \/    /  /      \      |    ___    |  /    ______|  .
         \              /  /   /\   \ .   |   |___>   |  \    \
   .      \            /  /   /__\   \    |         _/.   \    \            +
           \    /\    /  /            \   |   |\    \______>    |   .
            \  /  \  /  /    ______    \  |   | \              /          .
 .       .   \/    \/  /____/      \____\ |___|  \____________/
                               .                                        .
     .                           .         .               .                 .
                .                                   .            .
          .                            .                      .
  .                  .             -)------+====+       .
                           -)----====    ,'   ,'   .                 .
              .                  `.  `.,;___,'                .
                                   `, |____l_\
                    _,.....------c==]""______ |,,,,,,.....____ _
    .      .       "-:______________  |____l_|]'''''''''''       .     .
                                  ,'"",'.   `.
         .                 -)-----====   `.   `.
                     .            -)-------+====+       .            .
             .                               

"""

#%% Lecture Fichier csv

def Read():
    #Read data
    data=[]
    file=open('position_sample.csv','r')
    for line in file:
        try:
            line=[float(i) for i in line.strip('\n').split(';')]
            data.append(line)
        except ValueError:
            pass
    return data

#%% Individu

""" 
    Individu = [p1,p2,p3,p4,p5,p6]
    Fitness = Mean(Erreur_de_position)
    Soit epsilon=3 la précision du calcul (nb de chiffres après la virgule)
"""

class Individu: 
    
    def __init__(self,val=None): #Initialisation de l'individu
        if val==None:
            self.val=[round(rd.uniform(-100,100),3) for i in range(0,6)]
        else:
            self.val=val
    
    def __str__(self): #Lecture de l'individu
        return str(self.val)
    
    def __mul__(self,other): #Opérateur de croisement '*'
        split=rd.randint(0,5)
        Child1=Individu(self.val[:split]+other.val[split:])
        Child2= Individu(other.val[:split]+self.val[split:])
        return Child1,Child2
    
    def __invert__(self): #Opérateur de mutation '~'
        mutated=Individu()
        for i in range(0,6):
            if rd.random()>=0.5:
                mutated.val[i]=self.val[i]
        return mutated

    def position(self,t):
        x=self.val[0]*math.sin(self.val[1]*t+self.val[2])
        y=self.val[3]*math.sin(self.val[4]*t+self.val[5])
        return x,y
    
    def distance(x1,y1,x2,y2):
       return ((x1-x2)**2+(y1-y2)**2)**(1/2)

    def calc_fit(self):
        self.fitness=0
        for values in data:
            pos_test=self.position(values[0])
            self.fitness+=Individu.distance(pos_test[0],pos_test[1],values[1],values[2])
        self.fitness/=len(data)
        return self.fitness

        

#%% Population

def pop_init(size):
    return [Individu() for i in range(0,size)]        
        
def evaluate(pop):
    return sorted(pop,key=Individu.calc_fit)

def Mating(pool):
    Children=[]
    rd.shuffle(pool)
    Children_tuple=[pool[i-1]*pool[-i] for i in range(1,len(pool)+1)]
    for i in Children_tuple:
        Children.append(i[0])
        Children.append(i[1])
    return Children
    
def Mutating(pool):
    return [~i for i in pool]
    
def next_pop(eval_pop,size):
    # Pools
    Best_pool=eval_pop[:size//20]
    Ok_pool=eval_pop[:size//5]
    Mating_pool=Ok_pool
    # Operate
    pop=Best_pool+Mating(Mating_pool)+Mating(Best_pool)
    pop+=Mutating(pop)
    # Repopulating
    New=[Individu() for i in range(size-len(pop))]
    pop+=New
    return pop

#%% UI

# def Launch():
#     sg.theme('Black')
#     layout = [[sg.Text('Theme Browser')],
#               [sg.Text('Click a Theme color to see demo window')],
#               [sg.Listbox(values=sg.theme_list(), size=(20, 12), key='-LIST-', enable_events=True)],
#               [sg.Button('Exit')]]
#     window = sg.Window('Theme Browser', layout)


#%% Structures

def Genetic_Algorithm(size=1000,restart=None):
    pop=evaluate(pop_init(size)) if restart==None else restart
    gen=0
    t0=round(time.time(),1)
    repeat=0
    while repeat<500:
        prev_best=pop[0].val
        gen+=1
        tn=round(time.time()-t0,1)
        pop=next_pop(evaluate(pop),size)
        repeat=repeat+1 if (pop[0].val) == prev_best else 0
        print('Generation :',gen,' Time elapsed :',tn,'Best candidate fitness:',pop[0].fitness)
    return pop[0],gen,tn

def Loop(iterations):
    result=[]
    averages=[]
    av_gen=0
    av_time=0
    t0=time.time()
    for i in range(iterations):
        print('\n\n___________________________________________________________')
        print('\nIteration n°'+str(i)+" of the genetical algorithm:\n")
        print('___________________________________________________________\n')
        res_i=Genetic_Algorithm()
        result.append(res_i[0])
        averages.append(res_i[1:])
    eval_result=evaluate(result)
    for i in averages:
        av_gen+=i[0]
        av_time+=i[1]
    av_gen/=iterations
    av_time/=iterations
    print('\n\n___________________________________________________________')
    print("\nResults of "+str(iterations)+" iterations of genetical algorithms:\n")
    print('Average gen:'+str(round(av_gen,2))+'  Average time:'+str(round(av_time,1)))
    print('Total elapsed time:'+str(round(time.time()-t0,1)))
    print('Best fitness found:'+str(eval_result[0].fitness))
    print('Best candidate:\n'+str(eval_result[0].val))
    return eval_result

#%% Plot

def Plot(Obj):
    t=[i[0] for i in data]
    x=[i[1] for i in data]
    y=[i[2] for i in data]
    prediction=[Obj.position(i) for i in t]
    x_p=[i[0] for i in prediction]
    y_p=[i[1] for i in prediction]
    plt.subplot(3,1,1)
    plt.plot(x,color='black')
    plt.plot(x_p)
    plt.subplot(3,1,2)
    plt.plot(y,color='black')
    plt.plot(y_p)
    plt.subplot(3,1,3)
    plt.plot()
    plt.show()
        
    
#%% Main

if __name__=='__main__':
    import random as rd
    import matplotlib.pyplot as plt
    import math
    import time
    data=Read()
    iterations=50
    size=1000
    result=Loop(iterations)
    Best=result[0]
    Best_opti=Optimisation(Best)
    Plot(result[0])


#%% Debug
    # Indiv1=Individu()
    # Indiv2=Individu()
    # data=Read()
    # size=100
    # Pop1=pop_init(size)
    # eval_pop1=evaluate(Pop1)
    # Pop2=next_pop(eval_pop1,size)  
    # print('Population Initiale')
    # print(Pop1,'\n')
    # print('Population évaluée :',)
    # print(eval_pop1,'\n')
    # print('Population fille :')
    # print(Pop2,'\n')
    # p_worst=Individu([4.476, 0.43, 56.094, -12.962, 21.199, 92.772])
    # p_best=Individu([13.197, 21.098, 33.426, -22.902, 41.1, -25.284])
    # Plot(p_worst)
    # Plot(p_best)
    # result=Genetic_Algorithm(size)
    # Plot(result)
    

#%% Sauvegardes

    # Candidats

#p=Individu([4.476, 0.43, 56.094, -12.962, 21.199, 92.772]) #Fitness=1.380874838286586;
#p=Individu([12.763, 21.126, -86.095, -22.0, -41.082, 66.083]) #Fitness=0.923609721042281;
#p=Individu([5.614, -0.252, -72.092, 13.014, 21.165, 8.058]) #Fitness=0.8477212410648806;
#p=Individu([5.955, -0.207, 3.218, -13.102, -21.043, -21.032]) #Fitness=0.7535468860981592;
#p=Individu([-13.207, 21.088, 36.598, 22.911, -41.069, -43.919]) #Fitness=0.7535468860981592;
#p=Individu([13.186, 21.11, -54.577, 22.886, -41.065, 44.041]) #Fitness=0.7152500669835036;
#p=Individu([-13.213, 21.096, -57.675, 22.904, 41.1, 21.841]) #Fitness=0.16194224902806897;
#p=Individu([13.198, 21.098, 33.426, -22.903, 41.1, -25.284]) #Fitness=0.14647946960298727;

    # Populations

#pop=

    
#%% Optimisation locale

def Add(Obj,rank):
    return Individu(Obj.val[:rank]+[Obj.val[rank]+.001]+Obj.val[rank+1:])

def Sub(Obj,rank):
    return Individu(Obj.val[:rank]+[Obj.val[rank]-.001]+Obj.val[rank+1:])

def Optimisation(Obj):
    Optimised=[]
    for i in range(0,6):
        Up=Add(Obj,i)
        Down=Sub(Obj,i)
        if Up.calc_fit()<Obj.calc_fit():
            Prev=Up
            Next=Add(Prev,i)
            while Next.calc_fit()<Prev.calc_fit():
                Prev=Next
                Next=Add(Prev,i)
            print('Valeur optimisée de p'+str(i)+'='+str(Prev.val[i]))
            Optimised.append(Prev.val[i])
        elif Down.calc_fit()<Obj.calc_fit():
            Prev=Down
            Next=Sub(Prev,i)
            while Next.calc_fit()<Prev.calc_fit():
                Prev=Next
                Next=Sub(Prev,i)
            print('Valeur optimisée de p'+str(i)+'='+str(Prev.val[i]))
            Optimised.append(Prev.val[i])
        else:
            print('Valeur optimisée de p'+str(i)+'='+str(Obj.val[i]))
            Optimised.append(Prev.val[i])
    Indiv_opti=Individu(Optimised)
    return Indiv_opti.val,Indiv_opti.calc_fit()
    

    
    

            
