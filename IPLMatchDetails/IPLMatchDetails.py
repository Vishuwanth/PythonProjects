tot_matches = int(input())
matches_list = []

def getTeamsList(matches_list):
    teams = []
    for each in matches_list:
        if each[0] not in teams:
            teams.append(each[0])
        if each[1] not in teams:
            teams.append(each[1])
    return teams
    
for i in range(tot_matches):
    match = input().split(";")
    matches_list.append(match)
#print(matches_list)

def Sort(sub_li):
    return(sorted(sub_li, key = lambda x: x[-1],reverse=True)) 


def getTeamDict(team):
    team_dict = {
        "Team" : team,
        "Matches Played":0,
        "Won": 0,
        "Lost" : 0,
        "Draw": 0,
        "Points":0
    }
    for each in matches_list:
        if team in each[0]:
            team_dict["Matches Played"] +=1
            if each[2] == "loss":
                team_dict["Lost"] +=1
            elif each[2] == "win":
                team_dict["Won"] +=1
                team_dict["Points"] +=3
            else:
                team_dict["Draw"] +=1
                team_dict["Points"] +=1
        elif team in each[1]:
            team_dict["Matches Played"] +=1
            if each[2] == "loss":
                team_dict["Won"] +=1
                team_dict["Points"] +=3
            elif each[2] == "win":
                team_dict["Lost"] +=1
            else:
                team_dict["Draw"] +=1
                team_dict["Points"] +=1
    return team_dict

teams_list = getTeamsList(matches_list)
#print(teams_list)
if len(teams_list) == 0:
    print("No Output")
else:    
    all_list = []
    for each in teams_list:
        teams_dict = getTeamDict(each)
        lists =[]
        for k,v in teams_dict.items():
            lists.append("{}: {}".format(k,v))
        all_list.append(lists)
    
    all_list = Sort(all_list)
    for each in all_list:
        print(", ".join(each))