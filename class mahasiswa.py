class Mahasiswa:
    def __init__(self,n1='',n2=''):
        self.nama=n1
        self.nim=n2
    def setNama(self,newNama):
        self.nama=newNama
    def setNim(self,newNIM):
        self.nim=newNIM
    def getNama(self):
        return self.nama
    def getNim(self):
        return self.nim
    def tampilkan(self):
        print('Nam a= ',self.nama)
        print('NIM = ',self.nim)

mhs=Mahasiswa()
mhs.tampilkan()
mhs.setNama('bambang')
mhs.setNim(170411100150)
print(mhs.getNama())
print(mhs.getNim())

