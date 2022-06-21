class Hayvan():
    def __init__(self,cins,boy,kilo,yaş):
        self.cins = cins
        self.boy = boy
        self.kilo=kilo
        self.yaş = yaş
    def __str__(self):
        return(self.cins + str(self.boy) + str(self.kilo) + str(self.yaş))
class kus(Hayvan):
    def __init__(self,cins,boy,kilo,yaş,kanat_acıklıgı):
     super().__init__(cins,boy,kilo,yaş)
     self.kanat_acıklıgı = kanat_acıklıgı

    def __str__(self):
         return (self.cins + str(self.boy) + str(self.kilo) + str(self.yaş)) + str(self.kanat_acıklıgı)
reis = Hayvan("cocker",40,15,7)
print(reis)
ebabil =kus("muhabbet",7,1,3,12)
print(ebabil)