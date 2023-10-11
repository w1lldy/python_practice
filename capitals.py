# знаю, что по-уродски выглядит, заметки для будущего себя:
# 1) избавься от множества break UPD:от флага избавился
# 2) возможна ли рандомизация 1-ых значений словарей без преобразования в список
# (модуль рандом вроде не работает со словарями)
# 3) другую чушь вроде почистил
import random
capitals_dict = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
                 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
                 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
                 'Georgia': 'Atlanta', }
random_capital = []
for capital, state in capitals_dict.items():  # фу костыль
    random_capital.append(capital)
RC = random.choice(random_capital)
answer = input(f"Input state of {RC}\n").lower()
while (answer):  # вообще коляска
    if (answer == "exit"):
        print("Goodbye")
        break
    elif (answer == capitals_dict[RC].lower()):
        print('Correct!')
        break
    else:
        print('Incorrect! Try again!')
        answer = input().lower()
