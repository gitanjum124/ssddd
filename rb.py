class date:
    def __init__(self,a,b,c):
        self.d=a
        self.m=b
        self.y=c
    def day(self):
        print("Day=",self.d)
    def month(self):
        print("month:",self.m)
    def year(self):
        print("year=",self.y)
    def monthName(self):
        arr=["jan","feb","mer","apr","may","jun","july","aug","sep","oct","nov","dec"]
        print("monthName=",arr[self.m])
d1=date(10,7,2001)
d1.day()
d1.month()
d1.monthName()
