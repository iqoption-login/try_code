


class TryCode:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def sum(self):
        z = str(self.x + self.y)
        return f'Your Sum is {z}'
        
        
    def hello(self, name):
        expo = self.x**self.y
        print(f'Salut {name} you have expo {expo}')
        print("C'est du salut car on paroe Français")
        
if __name__ == "__main__":
    
    x = 2
    y = 3
    try_ = TryCode(x = x, y = y)
    
    print('sum :', try_.sum())
    
    try_.hello('Jordan')
    
    
    
    