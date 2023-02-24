class Testing:
    def __init__(self) -> None:
        print('I am inside init')
        
    def __enter__(self):
        print('i am inside enter doing something')
        
    def __exit__(self, exc_type, exc_value, exc_traceback):
        print("i am inside exit")
 


if __name__ == "__main__":
    with Testing() as t1:
        print('with statement block')
        
    
        
        
        