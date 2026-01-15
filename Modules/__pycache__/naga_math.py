naga_pi = 3.141592653589793

def naga_factorial(num):
    facto=1 
    while num > 0:
        facto *=num
        num-=1
    return facto

print(naga_factorial(7))
print(naga_pi)

from naga_math import naga_factorial as nf
print(nf(11))   
