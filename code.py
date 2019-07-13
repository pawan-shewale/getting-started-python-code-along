# --------------
import yaml

# Read the data of the format .yaml type
with open(path,'r') as f:
    data = yaml.load(f)
# Find data type of the file

print(type(data))

print("=================")
#print(match_details)
data_list=data.keys()
print(data_list)

# In which city, and at which venue the match was played and where was it played ?
print(data["info"]['city'])
print(data['info']['venue'])
# Which are all the teams that played in the tournament ? How many teams participated in total?
print(str(len(data['info']['teams']))+" teams played this match.")
print("Teams played in tournament are " +(data['info']['teams'][0])+" and  "+ (data['info']['teams'][1]))
# Which team won the toss and what was the decision of toss winner ?
print((data['info']['toss']['winner'])+" has won the toss and decided to "+data['info']['toss']['decision'])
print('=============================')
# Find the first bowler and first batsman who played the first ball of the first inning

  
for key,val in data.items():
    if key=='innings':
        #print(key)
        new_dict = val[0]['1st innings']['deliveries'][0][0.1]
        print(type(new_dict))
        print(new_dict['batsman'])
        print(new_dict['bowler'])
# How many deliveries were delivered in first inning ?
        delivery_count= val[0]['1st innings']['deliveries']
        print(type(delivery_count))
        print(len(delivery_count))
# How many deliveries were delivered in second inning ?
        delivery_count= val[1]['2nd innings']['deliveries']
        #print(type(delivery_count))
        print(len(delivery_count))

print((data['info']['outcome']['winner'])+" won by"+str(data['info']['outcome']['by']['runs']))
        


# Which team won and how ?



