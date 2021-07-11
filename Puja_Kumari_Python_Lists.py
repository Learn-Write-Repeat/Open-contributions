colors = ['red', 'blue', 'green']
print (colors[0])   
print (colors[2])    
print (len(colors))  
b = colors   
squares = [1, 4, 9, 16]
sum = 0
for num in squares:
    sum += num
print (sum) 
list = ['larry', 'curly', 'moe']
if 'curly' in list:
    print ('yay')
for i in range(100):
    print (i)
i = 0
while i < len(b):
    print (b[i])
    i = i + 3
list = ['larry', 'curly', 'moe']
list.append('shemp')         
list.insert(0, 'xxx')        
list.extend(['yyy', 'zzz'])  
print (list)  
print (list.index('curly'))   
list.remove('curly')        
list.pop(1)                  
print (list)
list = [1, 2, 3]  
list.append(4)
print (list)
list = []          
list.append('a')   
list.append('b')
list = ['a', 'b', 'c', 'd']
print (list[1:-1])  
list[0:2] = 'z'   
print (list)        