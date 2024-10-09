class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory
    
    @property
    def cpu(self):
        return self.__cpu
    
    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @property
    def memory(self):
        return self.__memory

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        return f"Выполняются вычисления: CPU * Memory = {self.__cpu * self.__memory}"

    def __str__(self):
        return f"Компьютер: CPU - {self.__cpu}, Memory - {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list
    
    @property
    def sim_cards_list(self):
        return self.__sim_cards_list
    
    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self,sim_card_number, call_to_number):
        if 1 <= sim_card_number <= len(self.__sim_cards_list):
            sim_card = self.__sim_cards_list[sim_card_number - 1]
            return f"Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim_card}"
        else:
            return "Неверный номер сим-карты"

    def __str__(self):
        return f"Телефон: Сим-карты - {', '.join(self.__sim_cards_list)}"

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    @staticmethod
    def use_gps(location):
        return f"Строится маршрут до локации: {location}"

    def __str__(self):
        return f"Смартфон: CPU - {self.cpu}, Memory - {self.memory}, Сим-карты - {self.sim_cards_list}"


# Создание объектов
computer = Computer(16, 500)
phone = Phone(["Beeline", "O!"])
smartphone1 = SmartPhone(8, 64, ["Beeline"])
smartphone2 = SmartPhone(6, 128, ["MegaCom", "O!", "Beeline"])

# Вывод информации об объектах
print(computer)
print(phone)
print(smartphone1)
print(smartphone2)

# Использование методов
print(computer.make_computations())
print(phone.call(1, "+996 777 99 88 11"))
print(smartphone1.use_gps("Бишкек, проспект Чуй"))
print(smartphone2.make_computations())
print(smartphone2.call(2, "+996 500 33 77 55"))

# Сравнение объектов Computer
print(computer > smartphone1)
print(computer <= smartphone2)
print(smartphone1 != smartphone2)