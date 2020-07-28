class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        return self.first + self.second

    def sub(self):
        return self.first - self.second

    def mul(self):
        return self.first * self.second

if __name__ == "__main__":
    fcall = FourCal()
    fcall.setData(30, 40)
    print(fcall.first, fcall.second)
