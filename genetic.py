import numpy as np
Pc=0.85
Pm=0.15
N=50
children=[]
parent=[]

for i in range(N):
    parent.append(np.random.uniform(-1,1))



def get_phenotype(x):
    Y = 3.5 * x - 4.1 * x * np.cos( 39 * x ) + 2.8 * np.sin( 4.6 * x )
    return Y

def get_genotype(x):
    x = int( x * (2 ** 20) )
    if x>0:
        x=bin(x ^ (x >> 1))
        x = int(x[2:])
    else:
        x = bin( np.abs(x) ^ (np.abs(x) >> 1) )
        x = int( '-' + x[2:] )
    return x


def get_reverse(x):
    L=[]
    string=''
    for i in range(len(x)):
        if x[i]=='0':
            L.append('1')
        else:
            L.append('0')
        string=string+L[i]
    return string

def cross(parent,children):
    i=0
    np.random.shuffle(parent)
    while i < (len(parent)-1):
        if np.random.random()<Pc:
            flag=np.random.randint(20)
            a=str(parent[i])[:flag]
            b=str(parent[i])[flag:]
            a1=str(parent[i+1])[:flag]
            b1=str(parent[i+1])[flag:]
            children.append(a+b1)
            children.append(a1+b)
        i+=2
    return children

def mutation(children):
    print( children )
    i=0
    while i < (len(children)):
        if np.random.random()<Pm:
            j=np.random.randint(17)
            if children[i][0]=='-':
                children[i]= children[i][:j+1] + str( get_reverse( children[i][j + 1:j + 4] ) ) + children[i][j+4:]

            else:
                children[i] = children[i][:j + 1] + str( get_reverse( children[i][j + 1:j + 4] ) ) + children[i][j + 4:]

            i+=1

    return children

def return_from_gray(x):
    x=str(x)
    x=int(x,2)
    g=0
    if x > 0:
        while np.abs(x)>0:
            g=g ^ x
            x=x>>1
    else:
        x=np.abs(x)
        while np.abs(x)>0:
            g=g ^ x
            x=x>>1
        g=-g
    g=g/(2**20)
    return g

def redution(children,parent):
    child=[]
    looser=[]
    for i in range(len(parent)):
        children.append(parent[i])
    np.random.shuffle(children)
    for i in range(len(children)):
        child.append(return_from_gray(children[i]))
    new_population=[]
    gen_new_population=[]
    j=0
    while j < (len(child)-1):
        if get_phenotype(child[j]) < get_phenotype(child[j+1]):
            new_population.append(child[j+1])
            gen_new_population.append(int(children[j+1]))
            looser.append(children[j])
        else:
            new_population.append(child[j])
            gen_new_population.append(int(children[j]))
            looser.append( children[j+1] )
        j+=2
    np.random.shuffle(looser)
    h=0
    while len(new_population)<50:
        new_population.append(return_from_gray(looser[h]))
        gen_new_population.append(int(looser[h]))
        h+=1
    new_population.sort()
    gen_new_population.sort()
    return new_population,gen_new_population

def phenotype_array(x):
    y=[]
    for i in range(len(x)):
        y.append(get_phenotype(x[i]))
    return y





