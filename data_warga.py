from latihan_oop import *

bapak1 = Warga('Firman','Jalan Mangga', 100000000)
# bapak1.gaji = 200000000
# bapak1.edit_gaji(1000000000)
# bapak1.info()

bapak2 = KetuaRT('Akbar','Jalan Lengkeng',300000000)
bapak3 = BendaharaRT('Uno', 'Jalan Rambutan', 100000000)

def fungsi_pengurus(RT):
    print(RT.tugas())
    
fungsi_pengurus(bapak1)