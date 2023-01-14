import random
import json 

data = {}
		
def shuffleArray(length):
    baseList = []
    for index in range(length):
        baseList.append(str(index + 1))

    random.shuffle(baseList)
    return baseList

def generate(length):
    for index in range(length):
        data[str(index + 1)] = shuffleArray(length)
    with open('./supergroup1.txt' , 'w') as f: f.write(json.dumps(data))
    return data