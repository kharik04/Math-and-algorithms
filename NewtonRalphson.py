######################### Newton Ralphson Script ##############################
#Author: Khariton Gorbunov
# User defines a function for which to compute the roots,
#and the script will return all roots of that function
###############################################################################
def function(x):#user defines
    expr=x**3-6*x**2+x+1
    return expr
def f(x, roots):
    expr=function(x) #this is the function of interest
    for root in roots:
        expr=expr/(x-root)#deflate expression by factoring out existing roots
    return(expr)

def dfdx(x, roots):#derivative of f(x)
    h=0.1
    df=(f(x+h, roots)-f(x-h, roots))/(2*h)#central difference method
    return df
    
def NewtRalph(x, tol, maxIt, roots):#arguments are initial guess, tolerance, max iterations and preexisting roots
    y=f(x, roots)
    n=0
    while(abs(y)>tol):
        m=dfdx(x, roots)
        x=-y/m+x
        y=f(x, roots)
        n=n+1
        if(n>maxIt):
            x=None
            break
    return(x)
root=0
roots=[]
while root!=None:
    try:
        root=NewtRalph(3,0.01,20,roots)
        roots.append(root)
    except:
        break
print("roots are:")
print(roots)