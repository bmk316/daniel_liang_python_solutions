import time


class Time:
    def __init__(self):
        self.setTime(int(time.time()))

    def getHour(self):
        return self.__hour

    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    def setTime(self, elapsedTime):
        self.__second = elapsedTime % 60
        totMins = elapsedTime // 60
        self.__minute = totMins % 60
        totHours = (totMins // 60) - 5
        self.__hour = (totHours % 24)


def main():
    currentTime = Time()
    print("Current time is " + str(currentTime.getHour()) + ":" + str(currentTime.getMinute()) + ":" + \
          str(currentTime.getSecond()))

    elapsedTime = eval(input("Enter the elapsed time: "))
    currentTime.setTime(elapsedTime)
    print("The hour:minute:second for elapsed time is " + str(currentTime.getHour()) + ":" + str(
        currentTime.getMinute()) + ":" + str(currentTime.getSecond()))


main()
