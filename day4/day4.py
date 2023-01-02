data = open("input.txt","r")
input_lines = data.readlines()

full = 0
non_overlap = 0


for line in input_lines:
    line = line.strip()
    first_group, last_group = line.split(',')

    first_start, first_end = first_group.split("-")
    first_start = int(first_start)
    first_end = int(first_end)

    last_start, last_end = last_group.split("-")
    last_start = int(last_start)
    last_end = int(last_end)

    if(first_start <= last_start and first_end >= last_end) or (last_start <= first_start and last_end >= first_end):
        full +=1

    elif(first_start < last_start and first_end < last_start) or (last_start < first_start and last_end < first_start):
        non_overlap +=1

print(full)
overlap = len(input_lines) - non_overlap
print(overlap)