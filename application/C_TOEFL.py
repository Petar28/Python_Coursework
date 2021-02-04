from Certificate import Certificate

# Certificate - TOEFL - характеристики:
class C_TOEFL(Certificate):
    def __init__(self,certificate_level, language):
      Certificate.__init__(self,certificate_level, language)
      #Тип:
      self.type = "TOEFL"
      #Страна:   
      self.c = "BUL"
      #Лицензионен номер на сертификата(TOEFL):
      self.license = "№ T-FL-417"


      