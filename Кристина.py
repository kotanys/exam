class Person():
    def __init__(self):
        self.money = 1000
        self.hamsters = []
        self.tired = False
        
    def buy_hamster(self, name, for_who, money):
        if self.money >= money:
            for_who.hamsters.append(name)
            self.money -= money
        else:
            self.work()
            self.buy_hamster(name, for_who, money)
        
    def kill(self):
        print(type(self).__name__ + " был убит")
        
    def work(self):
        self.money += 1000
        self.tired = True

class Kristina(Person):
    kristina_created = False
    
    def __init__(self):
        super().__init__()
        if Kristina.kristina_created:
            raise Exception("КРИСТИНА БЫВАЕТ ТОЛЬКО ОДНА! И ТОЛЬКО ОДНУ ЕЁ Я ЛЮБЛЮ 🤎")
        Kristina.kristina_created = True
    
    def get_love(self):
        return float("inf")
    
    def love_for(self, name):
        if name == "Вадим":
            return float("inf")
        else:
            return float("-inf")
        
    
    def get_my_hamsters(self):
        return self.hamsters
    
    def have_sex(self, who: Person):
        if type(who) == Vadim:
            if not who.tired:
                print("🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔞🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦💦")
            else:
                print(type(who).__name__ + " устал. Секса не будет")
        else:
            who.kill()
        
class Vadim(Person):
    def __init__(self):
        super().__init__()


k = Kristina()
v = Vadim()
k.have_sex(v)
for x in range(10):
    v.buy_hamster("Зажопа " + str(x), k, 300)
    print(k.get_my_hamsters())
k.have_sex(v)