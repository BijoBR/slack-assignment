# 2) Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.  
size =int(input("Enter the size of the list: ")) 
lst =[]
for i in range(size):
    value =int(input("Enter the value: "))
    lst.append(value)
def reverse():
    return lst[::-1]    
        
print(reverse())   

# Output:
# Enter the size of the list: 5
# Enter the value: 1
# Enter the value: 2
# Enter the value: 4
# Enter the value: 5
# Enter the value: 3
# [3, 5, 4, 2, 1]