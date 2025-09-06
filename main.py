print("Hello, Python Project!")
class Cal:
    def __init__(self, first, second):
        self.first=first
        self.second=second
    def pl(self):
        re=self.first+self.second
        return re
    def mi(self):
        re=self.first-self.second
        return re
    def mu(self):
        re=self.first*self.second
        return re
    def di(self):
        re=self.first/self.second
        return round(re,3)
    def print_a(self):
        print(f'덧셈결과: {self.pl()}')
        print(f'뺄셈결과: {self.mi()}')
        print(f'곱셈결과: {self.mu()}')
        print(f'나눗셈결과: {self.di()}')
a=Cal(5,7)
a.print_a()