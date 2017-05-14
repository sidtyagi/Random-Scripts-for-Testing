'''
Created on 14-May-2017

@author: sidtyagi
'''
my_str=''
inp_str= 'aabbbccaaaa'   
b=list(inp_str)
prev_char=b[0]
count=0
for x in b:  
    
    current_char=x
    
    print '-------Previous char is -----'+prev_char
    print '-------current char is ------'+current_char
    if prev_char==current_char:
            my_str+=x
            count+=1
    if prev_char!=current_char:
            my_str+=str(count)
            count=0
            count+=1
            my_str+=x
    
    prev_char=current_char
    print '*****************'
    print my_str
    print '++++++++++++++++++++++'
my_str+=str(count)
print my_str
