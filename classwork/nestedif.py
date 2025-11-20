teams=['csk','mi','srh','rcb','rr','kxip']
champions=[6,5,2,1,1,0]
print(teams)
ipl=True
if ipl:
    team=input().strip()
    if team in teams:
        index=teams.index(team)
        if champions[index]==0:
            print("Better luck next time")
        elif champions[index]==1:
            print("One time champion")
        elif 2<=champions[index]<=10:
            print("Conquerors")
        else:
            print("Future champions")
    else:
        print("Not in ipl")
else:
    print("watch ipl")
        
        
