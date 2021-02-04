from Certificate import Certificate

# Certificate - IELTS - характеристики:
class C_IELTS(Certificate):
    def __init__(self,certificate_level, language):
      Certificate.__init__(self,certificate_level, language)
      #Тип:
      self.type = "IELTS" 
      #Страна:   
      self.c = "BUL"
      #Лицензионен номер на сертификата(IELTS):
      self.license = "№ I-TS-891"

      


      


