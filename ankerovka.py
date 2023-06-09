    #    Расчет анкеровки по СП63
import numpy as np

while True:
    vid_arm = input("Выберите вид поверхности арматуры:\n (1)-Гладкая,\n (2)-Холоднодеформированная арматура периодического профиля,\n (3)-Горячекатаная и термомеханически обработанная арматура периодического профиля \n")
    
    if vid_arm == '1':
        n1 = 1.5
        break
    elif vid_arm == '2':
        n1 = 2.0
        break
    elif vid_arm == '3':
        n1 = 2.5
        break


my_list = list(range(70))
my_list1 = my_list[:33]
my_list2 = my_list[36:]

my_list1 = [str(i) for i in my_list1]
my_list2 = [str(i) for i in my_list2]

while True:
    diam_arm = input("Введите диаметр арматуры:\n")

    if diam_arm in my_list1:
        n2 = 1.0
        break
    elif diam_arm in my_list2:
        n2 = 0.9
        break

diam_arm = int(diam_arm)

As = (np.pi * (diam_arm/2)**2)                 #Площадь поперечного сечения анкеруемого стержня арматуры  см2

us = 2 * np.pi * (diam_arm/2)                   #Периметр поперечного сечения анкеруемого стержня арматуры   см

while True:
    class_beton = input('Введите класс бетона:\nB')    # Расчетное сопротивление бетона осевому растяжению  МПА   

    if class_beton == '12.5':
        Rbt = 0.66                                 # МПА
        break
    elif class_beton == '15':
        Rbt = 0.75
        break
    elif class_beton == '20':
        Rbt = 0.9
        break
    elif class_beton == '25':
        Rbt = 1.05
        break
    elif class_beton == '30':
        Rbt = 1.15
        break
    

Rbond = n1 * n2 * Rbt                         # Расчетное сопротивление сцепления арматуры с бетоном   МПА

while True:

    class_arm = input('Введите класс арматуры:\nА')

    if class_arm == '240':
        Rs = 215                                  # МПА
        break
    elif class_arm == '500':
        Rs = 435
        break

while True:
    
    a_kof = input('Введите коэффициент а, учитывающий влияние на длину анкеровки напряженного состояния бетона и арматуры: \n1 - для растянутых стержней, \n2 - для сжатых:\n')

    if a_kof == '1':
        a1 = 1
        break
    elif a_kof == '2':
        a1 = 0.75
        break
    
while True:
    
    if a_kof== '1':
        a2 = 1.2
        break
    elif a_kof == '2':
        a2 = 0.9
        break

l_0_an = (Rs * As)/(Rbond * us)


l_an = a1 * l_0_an 

l_an = round(l_an, 0)

l_nax = a2 * l_0_an

l_nax = round(l_nax, 0)

print(f'Длина анкеровки = {l_an} мм \nДлина нахлеста = {l_nax} мм')
input('Press ENTER to exit')
