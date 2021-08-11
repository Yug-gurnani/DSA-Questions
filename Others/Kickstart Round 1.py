# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 18:59:47 2020

@author: yuggu
"""

#Kickstart allocation problem
def kickstart():
    
    #No. of Test cases
    
    for i in range(int(input())):
        
        #no. of houses we can buy
        buy = 0
        #no. of houses and budget input
        num_of_house,budget = map(int,input().split())
        #list_of_house_prices
        houses = tuple(map(int,input().split()))
        #checking the number of houses we can buy
        if len(houses) > num_of_house:
            return
        for j in houses:
            if budget >= j:
                budget-=j
                buy += 1
        print('Case #{}: {}'.format(i+1,buy))
        

    
        
kickstart()
            
                
        
    
    