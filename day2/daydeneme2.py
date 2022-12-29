def round2(other_shape, me_shape):

        if ((scores[other_shape] == 1) ): #rock 
            scores[me_shape] = "Z" 

        elif (scores[other_shape] == 2): #paper 
            scores[me_shape] = "X"

        else: #makas
            scores[me_shape] = "Y"
    

    ###########
    def round2(other_shape, me_shape):
    if(scores[me_shape] == 1):
        print("kaybet karşim")

        if (other_shape == "A"):
            me_shape = "Z"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Lose"] + sum_value3
            return sum_value3

            

        elif (other_shape == "C"):
            me_shape = "Y"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Lose"] + sum_value2
            return sum_value3

        
        

    elif(scores[me_shape] == 2):
        print("beraber karşim")

        if (other_shape == "A"):
            me_shape = "X"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Draw"] + sum_value2
            return sum_value3

        
        

        elif (other_shape == "C"):
            me_shape = "Z"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Draw"] + sum_value2
            return sum_value3
        
        


    else:
        print("kazan be karşim")

        if (other_shape == "A"):
            me_shape = "Y"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Win"] + sum_value2
            return sum_value3
        
        

        elif (other_shape == "C"):
            me_shape = "Z"
            sum_value2 = scores[me_shape]
            sum_value3 = point_output["Win"] + sum_value2
            return sum_value3