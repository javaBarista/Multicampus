class AirForce:
    def __init__(self, name):
        self.name = name
        pass

    def take_off(self):
        pass

    def fly(self):
        pass

    def attack(self):
        pass

    def land(self):
        pass

class Boomber(AirForce):
    def __init__(self, name, bomb_cnt):
        super().__init__(name)
        self.bomb_cnt = bomb_cnt
        self.island = True

    def take_off(self):
        print("폭격기 %s 발진" % self.name)
        self.island = False

    def fly(self):
        print("폭격기 %s 비행" % self.name)

    def attack(self):
        for _ in range(self.bomb_cnt): print("폭탄 터~하!")

    def land(self):
        print("폭격기 %s 착륙" % self.name)
        self.island = True

    def bomb_add(self, cnt):
        if not self.island :
            print("보급하려면 착륙이 필요 합니다.")
            return

        self.bomb_cnt = cnt
        print("보급완료")

class Fighter(AirForce):
    def __init__(self, name, bomb_cnt):
        super().__init__(name)
        self.bomb_cnt = bomb_cnt
        self.island = True

    def take_off(self):
        print("전투기 %s 발진" % self.name)
        self.island = False

    def fly(self):
        print("전투기 %s 비행" % self.name)

    def attack(self):
        for _ in range(self.bomb_cnt): print("뚜두두두")

    def land(self):
        print("전투기 %s 착륙" % self.name)
        self.island = True

    def bomb_add(self, cnt):
        if not self.island :
            print("보급하려면 착륙이 필요 합니다.")
            return

        self.bomb_cnt = cnt
        print("보급완료")
