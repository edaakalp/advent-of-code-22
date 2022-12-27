data = open("input.txt","r")
input_lines = data.readlines()

#"A" : "Rock", "B" : "Paper", "C" : "Scissors","X" : "Rock", "Y" : "Paper", "Z" : "Scissors"

scores = {"A": 1, "B": 2, "C":3, "X": 1, "Y": 2, "Z":3}
point_output       = {"Lose":0, "Draw":3, "Win":6}

##AX-beraber        AY-Yener          CY-Cyener     
#BY-beraber         BZ-Zyener         AZ-Ayener
#CZ-beraber         CX-Xyener         BX-Byener 


def round(other_shape, me_shape):

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


    liste.append(round(splitted[0],splitted[1]))
print(sum(liste))


print(round("C","Z"))