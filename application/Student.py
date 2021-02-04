
#Клас СТУДЕНТ, съдържащ атрибути и методи:
class Student:
    def __init__(self, ID, name, university,zimen_semes, leten_semes,serti=None):
        self.ID = ID
        self.name = name
        self.university = university
        self.zimen_semes = zimen_semes
        self.leten_semes = leten_semes
        self.avg_year=0
        self.suma =0
        self.serti=serti
    
    #Взимане на оценките:
    def get_av(self):
      print(" Зимен семестър:", self.zimen_semes)
      print(" Летен семестър:", self.leten_semes)
      return " "

    #Взимане на данните на сертификата:
    def get_sertifikat(self):
        return f"{self.serti.get_level()} --> {self.serti.get_language()}  --> {self.serti.get_type_t()}  {self.serti.get_pr()} --> {self.serti.get_c()}"

      

#Студентът кандидатства с оценките си от ЗИМЕН и ЛЕТЕН СЕМЕСТЪР.
#Проверява се дали годишната му оценка е достатъчна да получава стипендия.

    def get_uspeh(self):
        p=self.zimen_semes
        s=self.leten_semes
        avg_year=((p+s)/2)

        if (avg_year > 4.5):
            #При одобрение надписът на съответния студент светва в ЗЕЛЕНО:
            print('\x1b[2;32;40m' + ' ----> ОДОБРЕН '  + '\x1b[0m',"Среден успех:" ,avg_year )
            #За всеки студен се получава различна стипендия в зависимост от успеха му:
            #Минималната стипендия за успех 4,5 е 675лв.
            #Стипендия за успех 6,00 достига 900лв.
            pari=self.suma
            #Формула от успех в средства:
            pari=(avg_year*100)*1.5

            #Подчертаване:
            def underline(line): 
              print("\033[21m {}\033[00m".format(line))

            #Ако има сертификат и успех(над 4,5)-> +100:
            if self.serti is not None: 
              print(" ИМА НАЛИЧЕН СЕРТИФИКАТ:")
              underline(self.get_sertifikat() )               
              print(" Студентът получава -->", pari,"+",100,"=",pari+100,"лв")
            else:
              print(" Студентът получава -->", pari,"лв")
            print("---------------------------------------")
            return " "
            
        else:
            #При отхвърляне надписът на съответния студент светва в ЧЕРВЕНО:
            print('\x1b[3;31;40m' + ' ----> НЕОДОБРЕН '  '\x1b[0m',"Среден успех:" ,avg_year)
            print("---------------------------------------")
            return " "

           

