data = open("input.txt","r")
input_lines = data.readlines()


lists = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

def elf_job(number, frm, to): #görevdagilimi
        frm_list = lists[frm]
        to_list = lists[to]
        items_to_move = frm_list[:number]
        for item in items_to_move:
            to_list.insert(0, item)
        del frm_list[:number]

def fill_container(line): #konteynurdakiler
    j = 0
    for i in range(1,34,4):
        j+=1
        if line[i] == " ":
            continue
        lists[j].append(line[i])



for (i,line) in enumerate(input_lines):
    line = line.strip("\n")
    if i < 8:
        fill_container(line)

    elif i >= 10 :
        line = line.split(" ")
        number = int(line[1])
        frm = int(line[3]) 
        to = int(line[5])

        elf_job(number, frm, to)
print("list1", lists)

str = ""
for list in lists.values():
    str += list[0]

#print(str)
#print(lists) #part 1

#part 2


lists2 = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[]}

def elf_job2(number, frm, to): #görevdagilimi
        frm_list = lists2[frm]
        to_list = lists2[to]
        items_to_move = frm_list[:number]

        items_to_move.extend(to_list)
        lists2[to] = items_to_move
        del frm_list[:number]

def fill_container2(line): #konteynurdakiler
    j = 0
    for i in range(1,34,4):
        j+=1
        if line[i] == " ":
            continue
        lists2[j].append(line[i])



for (i,line) in enumerate(input_lines):
    line = line.strip("\n")
    if i < 8:
        fill_container2(line)

    elif i >= 10 :
        line = line.split(" ")
        number = int(line[1])
        frm = int(line[3]) 
        to = int(line[5])

        elf_job2(number, frm, to)
#print("list2", lists2)

str2 = ""
for list in lists2.values():
    str2 += list[0]

print(str) #part 1
print(str2)

