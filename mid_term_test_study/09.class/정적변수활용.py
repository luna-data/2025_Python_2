class Television:
    serialNumber=0 #정적변수

    def __init__(self, channel, volume, on):
        Television.serialNumber+=1
        self.channel=channel
        self.volume=volume
        self.on=on
        self.mySerial=Television.serialNumber

    def show(self):
        print(f"채널: {self.channel},볼륨: {self.volume}, 전원: {self.on}, 시리얼번호: {self.mySerial}")

print('초기 시리얼 번호=',Television.serialNumber)

t1=Television(11,10,True)
t2=Television(7,20,False)
t3=Television(5,15,True)

t1.show()
t2.show()
t3.show()

print("마지막 시리얼 번호=",Television.serialNumber)

Television.serialNumber+=1
print("수동 증가 후 시리얼 번호=",Television.serialNumber)