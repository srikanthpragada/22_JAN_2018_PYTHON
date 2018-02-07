class Time:

    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s

    @property   #getter
    def seconds(self):
        return self.total_seconds()

    def total_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s

    def time_from_seconds(self, total):
        self.h = total // 3600
        total = total % 3600
        self.m = total // 60
        self.s = total % 60

    def __str__(self):
        return "%02d:%02d:%02d" % (self.h, self.m, self.s)

    def __eq__(self, other):
        # print(type(other))
        if isinstance(other, Time):
            return self.total_seconds() == other.total_seconds()
        else:
            return False

    def __gt__(self, other):
        return  self.total_seconds() > other.total_seconds()

    def __add__(self, other):
        total = self.total_seconds() + other
        t = Time()
        t.time_from_seconds(total)
        return t


t1 = Time(10, 2, 4)
t2 = Time(10,2,3)
secs = t1.total_seconds()
print(secs)
t1.time_from_seconds(secs)
print(t1 + 5000)



