class Football:

    def __init__(self, name, position = 0):
         self.name = name
         self.position = position

    def talk(self):
        print("Я", self.name, "стою на позиции:", self.position )

def main():
        crit1 = Football ("Максим Коваленко", "25 вратарь")
        crit1.talk()
        crit2 = Football ("Ивпн Коваленко", "4 защитник")
        crit2.talk()
        crit3 = Football ("Виталий Ермаков", "5 защитник")
        crit3.talk()
        crit4 = Football ("Михаил Шершень", "23 защитник")
        crit4.talk()
        crit5 = Football ("Ростислав Русин", "10 полузащитник")
        crit5.talk()
        crit6 = Football ("Дима Кравченко", "27 полузащитник")
        crit6.talk()
        crit7 = Football ("Артём Габелюк", "28 полузащитник")
        crit7.talk()
        crit8 = Football ("Фабиньо", "70 полузащитник")
        crit8.talk() 
        crit9 = Football ("Виталий Пономар", "7 нападающий")
        crit9.talk()
        crit10 = Football ("Илья Зубков", "19 нападающий")
        crit10.talk()
        crit11 = Football ("Марлисон", "33 нападающий")   
        crit11.talk()

main()