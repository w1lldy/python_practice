# знаю, что по-уродски выглядит, заметки для будущего себя:
# 1) избавься от множества break
# 2) возможна ли рандомизация 1-ых значений словарей без преобразования в список (модуль рандом вроде не работает со словарями)
# 3) 

import random
capitals_dict = {'Alabama': 'Montgomery', 'Alaska' : 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock',
'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
'Georgia': 'Atlanta',}
random_capital = []
flag = 1
for capital, state in capitals_dict.items(): # фу костыль
    random_capital.append(capital)
RC = random.choice(random_capital)
print(f"Input state of {RC}")
answer = input().lower()
while (flag != 0): # вообще коляска
    if (answer == "exit"):
        print("Goodbye"); flag = 1; break
    elif (answer == "test"):
        print('Correct!'); flag = 1; break
    else:
        print('Incorrect! Try again!'); answer = input().lower()
