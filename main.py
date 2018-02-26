import genetic as gen
import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    WIDTH = 800
    HEIGHT = 600
    DPI = 100
    f = open( 'text.csv', 'w' )
    f.close()
    f = open( 'text.csv', 'a' )

    def get_fx():
        x=-1
        y=[]
        xarray=[]
        while x<=2:
            y.append(gen.get_phenotype(x))
            xarray.append( x )
            x=x+0.005
        return xarray,y


    xarray, yarray = get_fx()
    n=8
    print( gen.parent )
    new = []


    for i in range(n+1):

        if i>=1:
            gen.parent=new
            gen.children=[]
        for j in range(len(gen.parent)):
            gen.parent[j] = gen.get_genotype(gen.parent[j])
        gen.children=gen.cross(gen.parent, gen.children)
        gen.children=gen.mutation(gen.children)
        new,gen_new=gen.redution( gen.children, gen.parent )
        new_array = gen.phenotype_array( new )
        print( gen.redution( gen.children, gen.parent ) )

        fig, ax = plt.subplots( num=None,
                                figsize=(WIDTH / DPI, HEIGHT / DPI),
                                dpi=DPI,
                                facecolor='w',
                                edgecolor='k' )
        fig.canvas.set_window_title( 'Генетический алгоритм' )

        if i==1 or i==3 or i==n:
            f.write('Population number =' + str(i) +'\n')
            f.write('Individ number; phenotype; genotype;f(x); F(x)'+'\n' )
            for r in range(len(new_array)):
                f.write('{number}; {new}; {gen_new};{new_array}; {new_array};'.format(number=r,new_array=new_array[r], gen_new=gen_new[r], new=new[r])+'\n')







        plt.xlabel( "x" )
        plt.ylabel( "y" )
        plt.plot( new, new_array ,'ro', label="практические значения" )
        plt.plot(xarray,yarray)
        plt.grid( True )
        plt.legend()
        plt.show()
    f.close()



