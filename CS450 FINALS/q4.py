class Fibonacci:
    def __init__(self):
        self.val = 0
        self.pre = 1

    def nxt(self):
        next_fib_num = Fibonacci()
        next_fib_num.val = self.val + self.pre
        next_fib_num.pre = self.val
        return next_fib_num

    def __repr__(self):
        return str(self.val)

def main():
    a = Fibonacci()
    print(a)             
    print(a.nxt())       
    print(a.nxt().nxt()) 
    print(a.nxt().nxt().nxt())  
    print(a.nxt().nxt().nxt().nxt())  
    print(a.nxt().nxt().nxt().nxt().nxt())  
    print(a.nxt().nxt().nxt().nxt().nxt().nxt())  
main()
