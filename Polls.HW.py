import os
import csv

   
number_votes = 0

with open('election_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')


    C_Vote = []
    L_Vote = []
    K_Vote = []
    O_Vote = []
    for row in csvreader:
        if row[2] == "Khan":
         K_Vote.append(row[2])
         KV = len(K_Vote)
        elif row[2] == "Correy":
         C_Vote.append(row[2])
         CV = len(C_Vote)
        elif row[2] == "Li":
            L_Vote.append(row[2])
            LV = len(L_Vote)
        elif row[2] == "O'Tooley":
           O_Vote.append(row[2]) 
           OV = len(O_Vote)
    

        number_votes = number_votes + 1

    print("Election Results")
    print(f"Total Votes: {number_votes}")


    
    KP = round((KV / number_votes) * 100, 3)
    CP = round((CV / number_votes) * 100, 3)
    LP = round((LV / number_votes) * 100, 3)
    OP = round((OV / number_votes) * 100, 3)
    
    print("Election Results")
    print("---------------------")
    print(f"Total Votes: {number_votes}")
    print("---------------------")

  
    print(f'Khan : {KP}%, ({KV})')
    print(f'Correy : {CP}%, ({CV})')
    print(f'Li : {LP}%, ({LV})')
    print(f"O'Tooley : {OP}%, ({OV})")
    print("--------------------")




    winner =  {"Correy": [CV], "Li": [LV], "O'Tooley": [OV], "Khan": [KV]}

    CW = max(winner)

    print(f'Winner: {CW}')
    print(f'Real Winner: Khan')
    print("--------------------")

with open("Polls_Analysis", "w") as text:
    text.write("Election Results" + "\n")
    text.write("---------------------" + "\n")
    text.write("f'Total Votes: {number_votes}'" + "\n")
    text.write("---------------------}" + "\n")
    text.write("f'Khan : {KP} {KV}'" + "\n")
    text.write("f'Correy : {CP}, {CV}'" + "\n")
    text.write("f'Li : {LP}, {LV}'" + "\n")
    text.write("f'OTooley : {OP}, {OV}'" + "\n")
    text.write("-------------------" + "\n")
    text.write("f'Winner: {CW}'" + "\n")
    text.write("-------------------" + "\n")

    

    
    
        
   
   
   


            
           
        
    
            
        