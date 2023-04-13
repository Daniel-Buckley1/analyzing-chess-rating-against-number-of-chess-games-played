import berserk
import matplotlib.pyplot as plt
session=berserk.TokenSession("lip_BqpyFevAtwnkbYNlJMFB")
client=berserk.Client(session=session)
info=client.users.get_live_streamers()
list=[]
games=[]
rating=[]
for dict in info:
    for key in dict:
        if key=="id":
            list.append(dict[key])


for name in list:
    
    bigdict=client.users.get_public_data(name)
    
    for key in bigdict:
        if key=="perfs":
            smallerdict=bigdict[key]
            for keyster in smallerdict:
                
                if keyster =="blitz":
                    smallestdict=smallerdict[keyster]
                    for ke in smallestdict:
                        if ke=="games":
                            games.append(smallestdict[ke])
                        if ke=="rating":
                            rating.append(smallestdict[ke])

print(games)
print(rating)
plt.scatter(games,rating)
plt.xlabel("Number of Games Played",fontsize=16)
plt.ylabel("Player Rating",fontsize=16)
plt.show()