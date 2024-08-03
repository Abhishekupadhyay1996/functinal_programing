class Fraction():
    def __init__(self,num,den):
        self.num=num
        self.den=den


    def __str__(self):
        return f"{self.num}/{self.den}"


    def __add__(self,other):
        result_num=(self.num*other.den) + (self.den*other.num)
        result_den=self.den*other.den
        return f"{result_num}/{result_den}"

    def __sub__(self,other):
        result_num=(self.num*other.den) - (self.den*other.num)
        result_den=self.den*other.den
        return f"{result_num}/{result_den}"


    def __mul__(self,other):
        result_num=(self.num*other.num)
        result_den=self.den*other.den
        return f"{result_num}/{result_den}"