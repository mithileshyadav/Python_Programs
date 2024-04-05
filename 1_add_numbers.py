# =========================================
# 1. Add two number's based upon user input
# =========================================

num1  = int(input("Enter First Number:"))
num2  = int(input("Enter Second Number:"))
print(f"Addition of {num1} and {num2} is: ",num1+num2)

# =========================================================================================
# 2. Add Infinite number's based upon comma separated user input using list comprehension #
# =========================================================================================

multiple_numbers = input("Enter Numbers with comma , separated: ").split(',')
all_sum = sum([int(i) for i in multiple_numbers])
print("Addition of all enterd number is :",all_sum)

# ================================================================
# 3. Add Infinite number's based upon comma separated user input #
# ================================================================

n_numbers = input("Enter Numbers with comma , separated: ").split(',')
sum_all = 0
for i in n_numbers:
    sum_all = sum_all+int(i)
print("Addition of all Entered Numbers: ",sum_all)

# ================================================================
# 4. Add Infinite number's based upon comma separated user input #
# ================================================================

n_numbers = input("Enter Numbers with comma , separated: ").split(',')
sum_all = 0
for i in n_numbers:
    sum_all = sum_all+int(i)
print("Addition of all Entered Numbers: ",sum_all)

# ===========================================================================
# 5. Add number's based upon User choice to ask add how many numbers to add #
# ===========================================================================

n_numbers = int(input("How many number you want to add: "))
string = 'Sum of '
sums = 0
for i in range(1, n_numbers+1):
    enterd_number = int(input(f"Enter {i} Number: "))
    sums = sums+enterd_number
    string = string + str(enterd_number)+", "
print(string [:-2]+ " is :",  sums)    # REMOVE LAST COMMA FROM THE STRING

# ===========================================================================================================
# 6. Add number's using Lamda Function based upon comma separated inputs
# Lambda function is an anonimous function it can take any number of arguments but return only one expresion
# ===========================================================================================================

sum_lambda = lambda list_of_all_nums : sum([int(i) for i in list_of_all_nums])
n_numbers = input("Enter Numbers with comma , separated: ").split(',')
result = sum_lambda(n_numbers)
print("Addtion of all Number is :",result)

# ==========================================================================================================
# 7. Add number's using reduce() lamda() Function and list comprehension, based upon space separated inputs
# reduce() comes under functools so import this and use this
# reduce(fun, sequence)
# At first step, first two elements of sequence are picked and the result is obtained 
# This proecess continues till no more elements are left in the container
# ==========================================================================================================

from functools import reduce
inputs = input("Enter multiple values with space separated :").split(" ")
lst = [int(i) for i in inputs]
print("Addtion of all number is : ", reduce(lambda a,b: a+b, lst))

# =============================================================
# 8. Add number's using class based programs
# =============================================================

class Addtion:
    def add(self):
        self.__sum = 0 # Intialize the private variable
        self.multiple_numbers = input("Enter Numbers with comma , separated: ").split(',')
        for i in self.multiple_numbers:
            self.__sum = self.__sum+int(i)
        print("Using class Based Addition of all Entered Numbers: ",self.__sum)
a = Addtion()
a.add()

# ====================================================================================
# 9. Add number's using class based programs use reduce() lambda() list compreshension
# Values Entered based upon comma separted based upon user choice
# ====================================================================================

from functools import reduce
class  Addition:
    def add(self):
        self._sum = 0 # Intialize the protected variable
        self.multiple_numbers = input("Enter Numbers with comma , separated: ").split(',')
        self.__all_number = [int(i) for i in self.multiple_numbers]
        print("Using class Based Addition of all Entered Numbers: ", reduce(lambda x,y : x+y, self.__all_number))
a = Addition()
a.add()









