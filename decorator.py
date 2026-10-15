def document_it(func):
    def wrapper(*args, **kwargs):
         print("this function name is ", func.__name__)
         return func(*args, **kwargs)
    return wrapper



#use the decorator
@document_it 
def some_func():
    print("some operation")
some_func()