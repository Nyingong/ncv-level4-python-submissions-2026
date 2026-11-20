#Passing a number and a list
def add_ten_number(n):
      n = n + 10
    
def add_ten_list(numbers):
      for i in range(len(numbers)):
          numbers[i] = numbers[i] + 10
    
x = 5
add_ten_number(x)
marks = [1, 2, 3]
add_ten_list(marks)
print(x, marks)
