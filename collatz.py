# Collatz Conjecture
# Cycle through all numbers, for each cycle:
# 1 - record steps to 1 for each number. 
# 2 - Record # of odd numbered steps, 
# 3 - Record # of even numbered steps, 
# 4 - Record highest number achieved


class Number:
    def __init__(self,number):
        self.starting_number = number
        self.current_number = number
        self.even_numbers = 0
        self.odd_numbers = 0
        self.steps_to_one = 0
        self.percentage_of_odd = 0
        self.percentage_of_even = 0
        self.highest_number = self.starting_number

    def number_odd(self,number):
        number = (number * 3) + 1
        return number

    def number_even(self,number):
        number = number // 2
        return number

    def calculate(self):
        while not self.current_number == 1:
            if (self.current_number % 2 == 0):
                self.current_number = self.number_even(self.current_number)
                self.steps_to_one += 1
                self.even_numbers += 1
                if self.current_number > self.highest_number:
                    self.highest_number = self.current_number
            else:
                self.current_number = self.number_odd(self.current_number)
                self.steps_to_one += 1
                self.odd_numbers += 1
                if self.current_number > self.highest_number:
                    self.highest_number = self.current_number
        if self.odd_numbers > 0:
            self.percentage_of_odd = round((self.odd_numbers/self.steps_to_one)*100,9)
        else:
            self.percentage_of_odd = 0

        if self.even_numbers > 0:
            self.percentage_of_even = round((self.even_numbers/self.steps_to_one)*100,9)
        else:
            self.percentage_of_even = 0

highest_number = [0,0] 
highest_steps = [0,0]
lowest_percentage_of_even = [0,100]
lowest_percentage_of_odd = [0,100]

print('Starting calculations...')
starting_integer = 618033988749894848
max_integer = 618033988749894849
for i in range(starting_integer,max_integer,1):
    print(f"Current Integer: {i} , Percent Complete: {round((i/(max_integer))*100,3)}%")
    number = Number(i)
    number.calculate()
    if number.highest_number > highest_number[1]:
        highest_number[1] = number.highest_number
        highest_number[0]= number.starting_number
    if number.steps_to_one > highest_steps[1]:
        highest_steps[1] = number.steps_to_one
        highest_steps[0] = number.starting_number
    if number.percentage_of_even < lowest_percentage_of_even[1]:
        lowest_percentage_of_even[1] = number.percentage_of_even
        lowest_percentage_of_even[0] = number.starting_number
    if number.percentage_of_odd < lowest_percentage_of_odd[1]:
        lowest_percentage_of_odd[1] = number.percentage_of_odd    
        lowest_percentage_of_odd[0] = number.starting_number

#f.close()
print(f"Highest number reached: {highest_number[1]} from seed {highest_number[0]} ")
print(f"Highest number of steps: {highest_steps[1]} from seed {highest_steps[0]} ")
print(f"Lowest percentage of even: {lowest_percentage_of_even[1]} from seed {lowest_percentage_of_even[0]} ")
print(f"Lowest percentage of odd: {lowest_percentage_of_odd[1]} from seed {lowest_percentage_of_odd[0]} ")