class Prima:
    def __init__(self,b1,b2):
        self.bilangan1 = b1
        self.bilangan2 = b2
    def hitungPrima(self):
        jumlah=0
        count=0
        a=[]
        print("> Perhitungan bilangan prima antara",self.bilangan1 ,"sampai",self.bilangan2,'=',end=' ')
        for i in range(self.bilangan1,self.bilangan2): 
            if i > 1: 
                for x in range(2,i): 
                    if (i % x) == 0: 
                        break 
                else:
                    jumlah=jumlah+i
                    a.append(i)
                    count+=1
        return jumlah,a,count
    def tampilkanPrima(self):
        print(self.hitungPrima()[1])
        
    def jumlahPrima(self):
        print(self.hitungPrima()[2])
    
       
a=int(input("Masukkan Bilangan 1 : "))
b=int(input("Masukkan Bilangan 2 : "))
p=Prima(a,b)
p.hitungPrima()
p.tampilkanPrima()
p.jumlahPrima()

