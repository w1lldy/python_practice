import statistics
# функция выделения 2 списков (зарегистрированные студенты и сведения об оплате)
def enrollment_stats():
    total_students = [list_list[1] for list_list in universities]
    total_tuition = [list_list[2] for list_list in universities]
    return total_students, total_tuition
# функция возврата среднего значения по спискам
def mean():
    return sum(res_1)/len(res_1), sum(res_2)/len(res_2)
# функция возврата медианы по спискам
def median():
    return statistics.median(res_1), statistics.median(res_2)

universities = [    # создание списка
      ['California Institute of Technology', 2175, 37704],
      ['Harvard', 19627, 39849],
      ['Massachusetts Institute of Technology', 10566, 40732],
      ['Princeton', 7802, 37000],
      ['Rice', 5879, 35551],
      ['Stanford', 19535, 40569],
      ['Yale', 11701, 40500]
               ] 
print("******************************")
res_1, res_2 = enrollment_stats()    # присваивание значений отдельным спискам для их работы
print(f"Total students: {sum(res_1):,}")
print(f"Total tuition: $ {sum(res_2):,}")
res_mean_1, res_mean_2 = mean()    # присваивание значений отдельным спискам для их работы
res_median_1, res_median_2 = median()    # присваивание значений отдельным спискам для их работы
print(f"Student mean: {res_mean_1:,.2f}")
print(f"Student median: {res_median_1:,}")
print(f"Tuition mean: $ {res_mean_2:,.2f}")
print(f"Tuition median: $ {res_median_2:,}")
