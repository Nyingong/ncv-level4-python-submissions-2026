data = [65, 72, 48, 90, 55, 72, 48, 72]

def total_of(values):
    total=0
    for vin values:
        total = total + v
    return total

def mean_of(values):
    return total_of(values)/len(values)

def max_of(values):
    best=values[0]
    for v in values:
        if v>best:
            best=v
    return best

def max_of(values):
    `best=values[0]
    for v in values:
        if v>best:
            best=v
    return best

def min_of(values):
    smallest=values[0]
    for v in values:
        if v<smallest:
            smallest=v
    return smallest

# Example data list so the code runs
def find_first(values, target):
    for i in range(len(values)):
        if values[i] == target:
            return i
    return -1

def find_all(values, target):
    positions = []
    for i in range(len(values)):
        if values[i] == target:
            positions.append(i)
    return positions

def count_of(values, target):
    count = 0
    for v in values:
        if v == target:
            count = count + 1
    return count

# Your corrected/runnable print statements
print("Total:", total_of(data))
print("Mean       :", mean_of(data))
print("Highest    :", max_of(data))
print("Lowest     :", min_of(data))
print("First 72 at:", find_first(data, 72))
print("All 72 at  :", find_all(data, 72))
print("Count of 72:", count_of(data, 72))
print("Mode       :", mode_of(data))
print("Mode (tie) :", mode_of([1, 2, 2, 3, 3]))