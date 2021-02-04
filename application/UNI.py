
#Клас УНИВЕРСИТЕТ(и техните данни), участващи в програмата за стипендии:
class UNI:
    def __init__(self, student_list,university_name, rector, number_students):
        self.student_list = student_list
        self.university_name = university_name
        self.rector = rector
        self.number_students = number_students


    #Статус:
    def print_uni(self):
        for student in self.student_list:
            print(" Статус на " + student.name +": ")
            print(student.get_av())
            print(student.get_uspeh())

    #1)  
    def get_avg(self):
        ocenka = 0
        ocenka2 = 0
        number_of_students = 0
        for student in self.student_list:
          ocenka += student.leten_semes
          ocenka2 += student.zimen_semes
          number_of_students += 1
        #Среден успех на всички студенти с точност до определен знак:
        round_num = round((((ocenka+ocenka2)/2) / number_of_students), 2)
        print("\n" +"1)Среден успех на кандидатствалите: "+ str(round_num))

    #2)
    #Използваме len за да определим броя на студентите:
    def get_num(self):
          print("2)Брой кандидатствали студенти: " + str(len(self.student_list)))

    #3)
    def get_percent(self):
        number_of_students = 0
        s = self.number_students
        for student in self.student_list:
          number_of_students += 1
        # s -> общ брой студенти в университета:
        num = ((number_of_students/s)*100)
        #Среден успех на всички студенти с точност до определен знак:
        round_num = round(num,2)
        print("3)Кандидатствали са",round_num,"%","от общия брой студенти на университета.")




