from karyawan import Karyawan

def main():
    kar1 = Karyawan("Dandi Setiawan", "IT", 5000)
    kar2 = Karyawan("Dinda Setiawati", "HR", 4000)
    kar3 = Karyawan("Jon Snow", "Direktur", 15000)

    print("Sebelum salary:")
    kar1.display_info()
    kar2.display_info()
    kar3.display_info()


main()
