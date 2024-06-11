#инкапсуляция - возможность программы скрыть атрибуты
class Persone:
    def __init__(self, FIO:str, age:int, salary:float):
        self.FIO = FIO
        self.age = age
        self.__salary = salary
    def Display(self) -> None:
        print(f"ФИО: {self.FIO}"
              f" возраст: {self.age}"
              f" зарплата: {self.__salary}")
    def get_salary(self) -> float:
        return self.__salary


objPersona1 = Persone("Иванов И.И." ,25 ,100000)
objPersona1.Display()

print(objPersona1.FIO) #атрибут открыт
# обращение к закрытому атрибуту - объект._имяКласса__имяАтрибута
print(objPersona1._Persone__salary)
print(objPersona1.get_salary())
objPersona1.FIO = "Petrov P.P"
objPersona1.Display()












