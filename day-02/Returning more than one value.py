def low_high(marks):
       low = marks[0]
       high = marks[0]
       for m in marks:
           if m < low:
               low = m
           if m > high:
               high = m
       return low, high
  
low, high = low_high([65, 72, 48, 90, 55])
print("Lowest:", low, "Highest:", high)

