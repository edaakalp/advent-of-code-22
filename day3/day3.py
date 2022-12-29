data = open("input.txt","r")
input_lines = data.readlines()

priority_sum = 0

def find_recurring(first, last):
    for i in first:
        for j in last:
            if i == j:
                return i
    
    return ""

def math(letter):
    number_letters = ord(letter)
    if number_letters >= 97:
        number_letters -= 96 
    else:
        number_letters -= 38 
    
    return number_letters


for line in input_lines:
    line = line.strip()
    half = int(len(line) / 2)
    first = line[:half]
    last = line[half:]

    recurring = find_recurring(first, last)
    priority = math(recurring)
    priority_sum += priority

print(priority_sum)

priority_sum2 = 0
#part2

def find_recurring2(first, middle, last):
    for i in first:
        for j in middle:
            for k in last:
                if i == j and j == k:
                    return i
    
    return ""

for x in range(0,len(input_lines), 3):
    line_first = input_lines[x].strip()
    line_second = input_lines[x+1].strip()
    line_last = input_lines[x+2].strip()

    recurring2 = find_recurring2(line_first, line_second, line_last)
    priority2 = math(recurring2)
    priority_sum2 += priority2

print(priority_sum2)
        










