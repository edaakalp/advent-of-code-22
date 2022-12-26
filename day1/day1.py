data = open("input.txt","r")
input_lines = data.readlines()

sum_calories = []
elf_calories = []
for line in input_lines:
    line = line.strip()
    if line != "":
        elf_calories.append(int(line))
    else:
        sum_calories.append(sum(elf_calories))
        elf_calories.clear()
    #print(line)


sum_calories.sort(reverse=True)
print(sum(sum_calories[:3]))