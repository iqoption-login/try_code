


class TryCode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def sum(self):
        return self.x + self.y
        
    def hello(self, name):
        expo = self.x**self.y
        print(f'Hello {name} you have expo {expo}')
        
        
if __name__ == "__main__":
    
    x = 2
    y = 3
    try_ = TryCode(x = x, y = y)
    
    print('sum :', try_.sum())
    
    try_.hello('Jordan')
    
    
    
    