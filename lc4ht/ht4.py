#Pост взрослого населения города X имеет нормальное распределение.
#Причем, средний рост равен 174 см, а среднее квадратичное отклонение равно 8 см.

#Какова вероятность того, что случайным образом выбранный взрослый человек имеет рост:
#а). больше 182 см
#б). больше 190 см
#в). от 166 см до 190 см
#г). от 166 см до 182 см
#д). от 158 см до 190 см
#е). не выше 150 см или не ниже 190 см
#ё). не выше 150 см или не ниже 198 см
#ж). ниже 166 см.

def z_value(height):
    return (height-174)/8
#a
from statistics import NormalDist
print(z_value(182))
NormalDist().cdf(z_value(182))
Pa=1-NormalDist().cdf(z_value(182))
print('вероятность того, что случайным образом выбранный взрослый человек имеет рост:больше 182 см = ', Pa)
#b
zb=z_value(190)
print(zb)
Pb=1-NormalDist().cdf(zb)
print('вероятность того, что случайным образом выбранный взрослый человек имеет рост:больше 190 см = ', Pb)
#в
zc1=z_value(166)
print(zc1)
zc2=z_value(190)
print(zc2)
Pc=NormalDist().cdf(zc2)-NormalDist().cdf(zc1)
print(Pc)
#г


