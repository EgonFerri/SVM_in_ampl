import random
import numpy as np
from sklearn.metrics import confusion_matrix
import pandas as pd


def generator(n):
    x=[]
    y=[]

    for i in range(n):
        x_val=[round(random.random(),3) for i in range(4)]
        stat=sum(x_val)
        
        if stat>2:
            result=1
        else:
            result=-1
        
        x.append(x_val)
        
        missclass=random.random()
        if missclass>0.05:
            y.append(result)
        else:
            y.append(-result)
    return(x, y)

def create_data(name, n, nu):
    f= open(name+'.dat',"w+")
    f.write('data;\n') 
    f.write('param n := '+str(n)+';\n')
    f.write('param m := '+str(4)+';\n')
    f.write('param nu := '+str(nu)+';\n')
    f.write('param x : 1 2 3 4 :=\n')
    x, y= generator(n)
    for i in range(n):
        f.write('\n')
        f.write(str(i+1)+' ')
        f.write(' '.join(map(str, x[i])))
    f.write(';\n')   
    f.write('param y:=\n')
    for i in range(n):
        f.write('\n')
        f.write(str(i+1)+' ')
        f.write(str(y[i]))
    f.write(';\n')     
    f.close() 
    
    
def predict(x_test, W, gamma):
    y_pred=[]
    for i in range(len(x_test)):
        stat=(np.matmul(np.array(x_test[i]),W)+gamma)
        if stat>0:
            y_pred.append(1)
        elif stat <0:
            y_pred.append(-1)
    return(y_pred)

def from_pred_to_stats(y_test, y_pred):
    cm1 = confusion_matrix(y_test,y_pred)
    accuracy=(cm1[0,0]+cm1[1,1])/len(y_test)

    sensitivity = cm1[0,0]/(cm1[0,0]+cm1[0,1])

    specificity=  cm1[1,1]/(cm1[1,0]+cm1[1,1])
    return([accuracy, sensitivity, specificity])