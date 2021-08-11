from segment_tree import SegmentTree 
  
# an array with some elements 
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11] 
  
# here we are fitting our array 
# into segment tree where t is  
# taken as object of segment tree 
# t will be used for perforfing  
# operations on that segmentTree 
  
t = SegmentTree(arr) 
  
# here we are finding value  
# of maximum number in a range 
a = t.query(2, 9, "max")  
print("The maximum value of this range is : ", a) 
  
  
# here we are finding the value  
# of mininum number in a range 
a = t.query(2, 9, "min")  
print("The minimum value of this range is : ", a) 
  
  
# here we are finding the value 
# of sum of a range 
a = t.query(2, 7, "sum")  
print("The sum of this range is : ", a) 
  
  
# here we are updating the value  
# of a particular index  
t.update(2, 25)  
  
# it will replace the value of 
# index '2' with 25 
print("The updated array is : ", arr) 