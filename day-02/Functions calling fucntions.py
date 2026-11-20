#functions calling functions
def total_of(marks):
       total = 0
       for m in marks:
           total = total + m
       return total
    
def average_of(marks):
       return total_of(marks) / len(marks)
    
print(average_of([65, 72, 48, 90, 55]))

