"""
kullanıcı terminal üzerinden 
1- yapılacak listesine madde ekle
    bir madde yapılcak işi , not alındığı tarihi ,süre sınırı(günlük-haftalık)

2- yapılacaklar listesini oku
    yapılması gereken işleri çıktı edicek. harici olarka ne zaman not alındığı ve bitme zamanına ne kadar kaldığını çıktı edicek

3- yapılcak iş tamamlandı
    yapılcak işin yapıldığını belirtmeyi sağlar. yapıldığı zaman , yapılmış işler dosyasına gider ve bitirme zamanı alır

4- yapılmış işleri oku
    yapılmış işler dosyasını okucak . bitirme tarihi ve kaç saatte bitirdiği yazıcak.

5- yapılmamış işleri oku
    zamanı geçmiş olan işleri görünteleyecek.

"""
from datetime import datetime
from datetime import timedelta
import json as js
import os


class todo:
    def __init__(self,work:str,final_date:dict):

        """
        work:  work to be done
        finish date : example {"hours": 1} or {"days" : 1}
        """
        self.work = work
        self.time_mode = "%H:%M  %d(%a)/%b/%Y"
        self.time =  datetime.now()
        self.start_date =self.time.strftime(self.time_mode)
        try:
            final = self.time + timedelta(hours= final_date["hours"] ) 
        except KeyError: 
            final = self.time + timedelta(days= final_date["days"] ) 

        self.fin_date = final
        self.finish_date = self.fin_date.strftime(self.time_mode)





