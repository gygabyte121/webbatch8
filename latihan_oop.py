# Bikin Class
class Warga:
    def __init__(self, nama, alamat, gaji):
        self.nama = nama
        self.alamat = alamat
        self.__gaji = gaji
    
    def info(self):
        '''
        menampilkan informasi dari warga
        '''
        print(f'nama warga: {self.nama} \n alamat: {self.alamat} \n gajinya: {self.__gaji}')
    
    def edit_gaji(self,gajinew):
        self.__gaji = gajinew

class KetuaRT(Warga):
    def tugas(self):
        return f'bapak {self.nama} mengatur iuran pemeliharaan lingkungan.'
        
    def informasi_ketua_rt(self):
        print(f'Ketua RT 001 adalah bapak {self.nama}')
        print(f'Ketua RT tinggal di {self.alamat}')
        
class BendaharaRT(Warga):
    def tugas(self):
        return f'bapak {self.nama} mengumpulkan iuran pemeliharaan lingkungan.'