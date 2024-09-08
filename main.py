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
todo_list_folder = os.getcwd() + "/todo lists"

#* this function creates the folder have the to do list json files at this file location also function creates json files in folder 
def json_file_maker():
    paths = []
    try: 
        os.mkdir(todo_list_folder)
    except FileExistsError:
        pass
    with open(todo_list_folder + "/todo_list.json","w",encoding="utf-8") as file:
        paths.append(os.path.abspath(todo_list_folder +"/todo_list.json")) 
        file.write("[]")

    with open(todo_list_folder + "/completed_tasks.json","w",encoding="utf-8") as file:
        paths.append(os.path.abspath(todo_list_folder + "/completed_tasks.json")) 
        file.write("[]")
    
    with open(todo_list_folder + "/not_completed_tasks.json","w",encoding="utf-8") as file:
        paths.append(os.path.abspath(todo_list_folder + "/not_completed_tasks.json")) 
        file.write("[]")
    return paths

json_files_paths = json_file_maker()



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





