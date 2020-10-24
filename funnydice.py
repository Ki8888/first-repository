from random import randrange
#!/usr/bin/env python3

class FunnyDice:
    def __init__(self,n=6):
        self.n=int(n)
        self.numbers=list(range(1,n+1))
        self.index=randrange(0,self.n)
        self.val=self.numbers[self.index]
        
    def throw(self):
        self.index=randrange(0, self.n)
        self.val=self.numbers[self.index]
    
    def getval(self):
        return self.val
    
    def setval(self, valnum):
        if valnum<=self.n:
            self.val=valnum
        else:
            print("Not in range,number can 1~{0}".format(self.n))
          
        
def main():
    n=get_inputs()
    mydice = FunnyDice(n)
    mydice.throw()
    print("Lucky number is {0}".format(mydice.getval()))
    
def get_inputs():
    n=int(input('input dice dimension numbers.'))
    return n

# 인터프리터에서 직접 실행했을 경우에만 if내의 코드를 돌려라.
if __name__ == '__main__':
    main()


    
