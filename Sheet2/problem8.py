'''
Write a function that accepts any number of positional and keyword arguments and
 prints them separately.
'''

def print_num(*args,**kwargs):
    
    for arg in args:
        print(arg)
        
    # for kwarg in kwargs:
    #     print(kwarg)
        
    for key,value in kwargs.items():
        print(f"{key} : {value}")
        
print_num(1,2,3,4,5,name='yaish',surname='raval',)