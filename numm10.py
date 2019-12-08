from math import pow

class complex_numbers:
    def __init__(self,real,imagin):
        self.real = real
        self.imagin = imagin

    def __add__(self,other):
        return complex_numbers(self.real + other.real, self.imagin + other.imagin)

    def __sub__(self,other):
        return complex_numbers(self.real - other.real, self.imagin - other.imagin)

    def __mul__(self,other):
        return complex_numbers(self.real * other.real, self.imagin * other.imagin)

    def __div__(self,other):
        try:
            return self.__mul__(complex(other.real, -1 * other.imagin)).__mul__(complex(1.0 / (other.mod().real) ** 2,0 ))
        except ZeroDivisionError as e:
            print(e)
            return None
    def mod(self):
        return complex_numbers(pow(self.real ** 2 + self.imagin ** 2, 0.5), 0)

    def __str__(self, precision = 2):
        return str('%.' + "%df" % precision) % float(self.real) + ("+" if self.imagin >= 0 else '-') + str("%." + "%df" % precision) % (float(abs(self.imagin))) + "i"

A = complex(*map(float, raw_input().strip().split()))
B = complex(*map(float, raw_input().strip().split()))


print(A + B)
print(A - B)
print(A * B)
print(A / B)
print(A.mod())
print(B.mod())

# import math
#
#
# class Complex:
#
#     def __init__(self, real, imaginary):
#         self.real = round(float(real), 2)
#         self.imaginary = round(float(imaginary), 2)
#
#     # def conjugate(self):
#     #     return other.real - other.imaginary
#
#     def __add__(self, other):
#         r = self.real + other.real
#         i = self.imaginary + other.imaginary
#         return Complex(r, i)
#
#     def __sub__(self, other):
#         r = self.real - other.real
#         i = self.imaginary - other.imaginary
#         return Complex(r, i)
#
#     def __mul__(self, other):
#         r = self.real * other.real - self.imaginary * other.imaginary
#         i = self.real * other.imaginary + self.imaginary * other.real
#         return Complex(r, i)
#
#     def __truediv__(self, other):
#         x = self.real * other.real + self.imaginary * other.imaginary
#         y = self.imaginary * other.real - self.real * other.imaginary
#         z = other.real ** 2 + other.imaginary ** 2
#         real = x / z
#         imag = y / z
#         return Complex(real, imag)
#
#     def mod(self):
#         r = math.sqrt(self.real ** 2 + self.imaginary ** 2)
#         # print(r)2
#         i = 0
#         return Complex(r, i)
#
#     def __str__(self):
#         if self.imaginary == 0:
#             result = "%.2f+0.00i" % (self.real)
#         elif self.real == 0:
#             if self.imaginary >= 0:
#                 result = "0.00+%.2fi" % (self.imaginary)
#             else:
#                 result = "0.00-%.2fi" % (abs(self.imaginary))
#         elif self.imaginary > 0:
#             result = "%.2f+%.2fi" % (self.real, self.imaginary)
#         else:
#             result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
#         return result
#
#
# if __name__ == '__main__':
#     c = map(float, input().split())
#     d = map(float, input().split())
#     x = Complex(*c)
#     y = Complex(*d)
#     print(*map(str, [x + y, x - y, x * y, x / y, x.mod(), y.mod()]), sep='\n')

