class Karyawan:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.__salary = salary #encapsulation

    def get_salary(self):
        return self.__salary

    def hitung_salary(self):
        if self.position == "IT":
            self.__salary *= 1.10
        elif self.position == "HR":
            self.__salary *= 1.15
        elif self.position == "Direktur":
            self.__salary *= 1.01
        else:
            print("Posisi tidak dikenali")
        
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: Confidential")
