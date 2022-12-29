data = open("input.txt","r")
input_lines = data.readlines()

#"A" : "Rock", "B" : "Paper", "C" : "Scissors","X" : "Rock", "Y" : "Paper", "Z" : "Scissors"

scores = {"A": 1, "B": 2, "C":3, "X": 1, "Y": 2, "Z":3}
point_output       = {"Lose":0, "Draw":3, "Win":6}

#AX-draw         AY-Y-lose          CY-C-win     
#BY-draw         BZ-Z-lose          AZ-A-win
#CZ-draw         CX-X-lose          BX-B-win 


def round1(other_shape, me_shape):

    if (scores[other_shape] == scores[me_shape]):
        sum_value = point_output["Draw"] + scores[me_shape]
        return sum_value
    
    elif ((scores[other_shape] - scores[me_shape] == -2) or (scores[other_shape] - scores[me_shape] == 1)):
        sum_value = point_output["Lose"] + scores[me_shape]
        return sum_value
       
    else:
        sum_value = point_output["Win"] + scores[me_shape]
        return sum_value


liste = []
for line in input_lines:
    line = line.strip()
    splitted = line.split(" ")

    liste.append(round1(splitted[0],splitted[1]))
print(sum(liste)) #part1


#part2  
scores2 = {"A": 1, "B": 2, "C":3, "X": 0, "Y": 3, "Z":6}

list2 = []

def round2(input1, output1):
    match output1:
        case 6:
            y = input1 % 3 + 1
        case 3:
            y = input1
        case 0:
            y = (input1 + 1) % 3 + 1

    total = y + output1

    return total

for line in input_lines:
    line = line.strip()
    shape_other, shape_me = line.split(" ")
    (input1, output1) = (scores2[shape_other], scores2[shape_me])
    kj = round2(input1, output1)
    list2.append(kj)

print(sum(list2))




