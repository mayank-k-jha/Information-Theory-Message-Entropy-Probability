# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:56:55 2017

@author: mayank
"""
import math
import matplotlib.pyplot as plt


def prob_in():
    prob_list=[]
    no=int(input('Enter no of Probabilty : '))
    typ=int(input('Enter 1 for decimal type probability entry or 2 for fraction type : '))
    if typ !=1 and typ!=2 :
        print('Invalid Input ')
        return
    for i in range(no):
        print('\n',i+1,'th Probabilty :')
        if typ==1:
            prob_list.append(float(input()))
        else :
            h=float(int(input())/(int(input())))
            prob_list.append(h)
    plt.plot(prob_list)
    plt.show()       
    return prob_list  

      

def Entropy(prob_list,b):
    if b :
        print('\nCalculating Entropy Of Message\n')
    entro=0
    for i in prob_list:
        if i !=0:
            entro+=(i*(math.log((1/i),2)))
    entro=('%.4f'%entro)    
    if b :
        print('Entropy for the Given Message Signal is : ',entro,'bits/message\n')
    return entro
        


def Rate_Of_Information():
    e=Entropy(prob_in(),False)
    r=int(input('Enter Rate Of Message : '))
    print('\nEntropy for the Given Message Signal is : ',e,'bits/message')
    print('Rate Of Information  : ',float(e)*float(r),'bits/second\n\n')
    return
    


def Matrix_entry():
    row=int(input("Enter no of Rows : "))
    col=int(input('Enter no of Column: '))
    Matrix = [[0 for x in range(col)] for y in range(row)] 
    print("Enter elements : \n")
    for i in range(row):
        print('row ',i+1,' elements : ')
        for j in range(col):
            Matrix[i][j]=float(input())
            
    return Matrix       
            
    
    

def Checking_Conditional_Probability(b):
    Matrix=Matrix_entry()
    row,col=len(Matrix),len(Matrix[0])    
    total=0
    row_ch=[0 for i in range(row)]
    col_ch=[0 for i in range(col)]
    for i in range(row):
        for j in range(col):
            ent=Matrix[i][j]
            total+=ent
            row_ch[i]+=ent     # Logical 
            col_ch[j]+=ent     # Amazing 
    r_ch,c_ch,=0,0 
    for i in row_ch:
         if i !=1:
             r_ch=1
             break
    for i in col_ch:
         if i !=1:
             c_ch=1
             break
    ret=0    
    if total >=.9 and total <=1 :
        ret=1
        if b :
            print('\nGiven Probability Matrix is : P(XY)\n')
    elif r_ch!=1 :
        ret=2
        if b :
            print('\nGiven Probability Matrix is : P(Y/X)\n')
    elif c_ch!=1 :
        ret=3
        if b :
            print('\nGiven Probability Matrix is : P(X/Y)\n')
    else :
        if b :
            print('\n\tGiven Matrix is Not Valid \n\n')
    plt.plot(Matrix)
    plt.show()    
    return ret,Matrix,row_ch,col_ch  
         
    


def h_xy(m):
    ans=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] !=0:
                ans+=(((.333)*m[i][j])*math.log((1/m[i][j]),2))
    return ans
 
def h_x_by_y(m) :
    # Converting to P(XY)
    ans=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] !=0:
                ans+=(((.333)*m[i][j])*math.log((1/m[i][j]),2))
            
    return ans

def h_y_by_x(m) :
    # Converting to P(XY)
    ans=0
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] !=0:
                ans+=(((.333)*m[i][j])*math.log((1/m[i][j]),2))
            
    return ans

    

def Finding_Conditional_Entropy():
    print("Enter probabilty Matrix : \n")
    opt,mat,p_x_list,p_y_list=Checking_Conditional_Probability(False)
    print('Calculating Entropy \n')
    ans,h_x,h_y=0,Entropy(p_x_list,False),Entropy(p_y_list,False)
    print('\n\tH(X) = ',h_x)
    print('\tH(Y) = ',h_y,'\n')
    if opt==0:
        return
    elif opt==1:
        print('Calculating H(XY) : ')
        ans=h_xy(mat)
        print('H(XY) = ',ans)
    elif opt==2:
        print('Calculating H(Y/X) : ')
        ans=h_y_by_x(mat)
        print('H(Y/X) = ',ans)
    elif opt==3:
        print('Calculating H(X/Y) : ')
        ans=h_x_by_y(mat)
        print('H(X/Y) = ',ans)
    else :
        print('Invalid Option')
        
    if opt!=0:
        oth=int(input('Enter 1 to Calculate another Condtional Entropies : '))
        if oth ==1 :
            if opt==1:
                print('\n\tCalculating H(Y/X) ')
                print('\tH(Y/X) = ',ans-float(h_x))
                print('\n\tCalculating H(X/Y) ')
                print('\tH(X/Y) = ',ans-float(h_y),'\n')
            elif opt==2:
                print('\n\tCalculating H(XY) ')
                print('\tH(XY) = ',ans+float(h_x))
                print('\n\tCalculating H(X/Y) ')
                print('\tH(X/Y) = ',ans+float(h_x)-float(h_y))
            else :    
                print('\n\tCalculating H(XY) ')
                print('\tH(XY) = ',ans+float(h_y))
                print('\n\tCalculating H(Y/X) ')
                print('\tH(Y/X) = ',ans+float(h_y)-float(h_x),'\n')
            
        else :
            return
        
    
    return
    
    
    

def about():
    print('\n\n\tThis is a Program based on INFORMATION THEORY  where we can')
    print('\tcalculate various parameters related to message based on its ')
    print('\tprobabilty distribution either alone or mutualy with respect ')
    print('\tto other message.')
    print('\n\t@author :\n')
    print('\tMAYANK KUMAR')
    print('\tB.Tech CSE A')
    print('\tRoll no : BETN1CS15059\n\n')
    return


    
print('\n\t  ADC Project Based Learning \n')
while(True):
    print('\nPLease select the operation to be performed :\n')
    print('\t1.Finding Entropy\n\t2.Rate Of Information\n\t3.Checking Conditional Probability\n\t4.Finding Conditional Entropy\n\t5.About\n\t6.Exit\n\n')
    option=int(input())
    if option==1:
        Entropy(prob_in(),True)
    elif option==2:
        Rate_Of_Information()
    elif option==3:
        Checking_Conditional_Probability(True)
    elif option==4:
        Finding_Conditional_Entropy()
    elif option==5:
        about()
    elif option==6:
        print('\tThank You for using Program, Good Bye \n')
        break
    else :
        print('Enter Correct choice \n')
        
        