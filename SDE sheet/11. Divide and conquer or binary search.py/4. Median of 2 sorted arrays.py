# using divide and conquer we divide 
# the 2 arrays accordingly recursively 
# till we get two elements in each  
# array, hence then we calculate median 
  
#condition len(arr1)=len(arr2)=n 
def getMedian(arr1, arr2, n):  
      
    # there is no element in any array 
    if n == 0:  
        return -1
          
    # 1 element in each => median of  
    # sorted arr made of two arrays will     
    elif n == 1:  
        # be sum of both elements by 2 
        return (arr1[0]+arr2[1])/2
          
    # Eg. [1,4] , [6,10] => [1, 4, 6, 10] 
    # median = (6+4)/2     
    elif n == 2:  
        # which implies median = (max(arr1[0], 
        # arr2[0])+min(arr1[1],arr2[1]))/2 
        return (max(arr1[0], arr2[0]) + 
                min(arr1[1], arr2[1])) / 2
      
    else: 
        #calculating medians      
        m1 = median(arr1, n) 
        m2 = median(arr2, n) 
          
        # then the elements at median  
        # position must be between the  
        # greater median and the first  
        # element of respective array and  
        # between the other median and  
        # the last element in its respective array. 
        if m1 > m2: 
              
            if n % 2 == 0: 
                return getMedian(arr1[:int(n / 2) + 1], 
                        arr2[int(n / 2) - 1:], int(n / 2) + 1) 
            else: 
                return getMedian(arr1[:int(n / 2) + 1],  
                        arr2[int(n / 2):], int(n / 2) + 1) 
          
        else: 
            if n % 2 == 0: 
                return getMedian(arr1[int(n / 2 - 1):], 
                        arr2[:int(n / 2 + 1)], int(n / 2) + 1) 
            else: 
                return getMedian(arr1[int(n / 2):],  
                        arr2[0:int(n / 2) + 1], int(n / 2) + 1) 
  
 # function to find median of array 
def median(arr, n): 
    if n % 2 == 0: 
        return (arr[int(n / 2)] +
                arr[int(n / 2) - 1]) / 2
    else: 
        return arr[int(n/2)]
"""
TC = o(log n)
SC = o(1)
"""