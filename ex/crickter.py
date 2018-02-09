
class Batsman:
    def __init__(self,name, runs =0):
        self.name = name
        self.runs = runs

    def __str__(self):
        return  "%s  %d" % (self.name, self.runs)


class Bowler:
    def __init__(self, name, wickets=0):
        self.name = name
        self.wickets = wickets

    def __str__(self):
        return "%s  %d" % (self.name, self.wickets)


class AllRounder(Batsman,Bowler):
    def __init__(self,name,runs, wickets):
        Batsman.__init__(self,name,runs)
        Bowler.__init__(self, name, wickets)

    def __str__(self):
        return "%s %d %d" % (self.name, self.runs, self.wickets)



c  = AllRounder("Abc",12000,300)
print(c)
print( dir(c))

