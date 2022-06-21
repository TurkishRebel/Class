
class Vechile:
 def __init__(self,ad,soyad,numara):
   self.ad = ad
   self.soyad = soyad
   self.numara = numara
   self.ad = self.ad.lower()
   self.soyad = self.soyad.lower()
 def sea(self):
   file = open("aa.txt")
   if len(str(self.numara)) == 9 and self.numara not in file.read():
    file = open("aa.txt","a",encoding="UTF-8")
    file.write(self.numara +  " : " +self.soyad + "_"  + str(self.ad ) + "\n")
    file.close()
    print("Kayıt başarılı!...")
   elif len(str(self.numara)) != 9:
    print("Numara dokuz karekterli olmalıdır!")
   else:
    print("Bu öğrenci numarası zaten kullanımda!")
ahmet = Vechile("Salih ","Şahin","192801030")
ahmet.sea()