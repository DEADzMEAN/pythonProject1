print("Программа сравнения бойза орка с космодесантником выбранного вами легиона <прямым столкновением в тестовом кубе>")

class Warior:
    def __init__(self, str, con, dex, men, int):
        self.str = str
        self.con = con
        self.dex = dex
        self.men = men
        self.int = int

    def __eq__(self, other):
        if self.str != other.str:
            return False
        elif self.con != other.con:
            return False
        return True

    def __lt__(self, other): #метод тыка показывает, чтое сли в лжном методе больше двух полян по посте сравнения первой
                            #эта тварь успокаивается возвращая результат
        if self.str < other.str:
            return True
        elif self.con < other.con: #если применить сей встроенный метод два раза не съебёт ли это логику классового подсчёта?!
            return True
        return False
       # return self.str < other.str
        #return self.con < other.str

#    def __lt__(self, other):        попробовал - полная шляпа - не работает
#        if self.int < other.int:
#            return True
#        return False
Orc_boiz1 = Warior(str= 36, con= 47, dex= 21, men= 27, int= 3)
Orc_boiz = Warior(str= 36, con= 47, dex= 21, men= 27, int= 4)
White_scars = Warior(str= 36, con= 32, dex= 35, men= 25, int= 13)
Space_woolf = Warior(str= 39, con= 42, dex= 32, men= 27, int= 20)
Night_lords = Warior(str= 33, con= 32, dex= 32, men= 25, int= 19)
Thousand_sons = Warior(str= 19, con= 32, dex= 28, men= 38, int= 50)
Alpha_legion = Warior(str= 28, con= 25, dex= 30, men= 27, int= 25)

if Orc_boiz1 == Orc_boiz:  #как воткнуть инпутом экземпляры класса я так и не нашёл
    print("силы равны")
else:
    print("щас кто-то кому-то даст пизды")

    if Orc_boiz < Orc_boiz1:
        print("Орк начинает всасывать")
    elif Orc_boiz1 < Orc_boiz:
        print("Orc_boiz1 соска - Бойзы рулят!")

#if input("1:") == input("2:"):     тут он сравнил просто цифры инпута- как прикрутить именно ссылку на экз класса не пойму
    #print("силы равны")
#else:
    #print("щас кто-то кому-то даст пизды")

#if Orc_boiz < Space_woolf:
    #print("Орк начинает всасывать")
#elif Space_woolf < Orc_boiz:
   # print("Космодес соска - Бойзы рулят!")

   #пытаюсь разобраться с гитом