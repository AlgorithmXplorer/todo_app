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

local_path = os.getcwd()

def json_files_maker(path):
    folder_path = f"{path}/todo_lists"

    def files():
        
        os.chdir(folder_path)
        
        with open(folder_path + "/todo_list.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")
        with open(folder_path + "/uncompleted_todos.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")
        with open(folder_path + "/completed_todos.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")

    
    if os.path.exists("todo_lists"):
        files() 
    else: 
        os.mkdir("todo_lists")
        os.system(f"attrib +h {'todo_lists'}")
        files() 
json_files_maker(local_path)

class todo_repo:
    def __init__(self,task:str ,date: int, formatter: str):
        """
        task : a str param. data about task
        date: this param should be a int. day week or hours
        formmatter: this param for format the date datas 
            "hour" - "day" - "week"
        """
        self.work = task
        self.deadline = date
        self.formatter = formatter
        self.dates = {"start date": None , "deadline": None , "finish date" : None}
    
    def deadline_maker(self):
        start_date = datetime.strptime(self.dates["start date"], "%c")

        if self.formatter == "hour":
            #*calculation of deadline
            deadline =  start_date + timedelta(hours = self.deadline )
            
            #* timedelta object changed to datetime object
            deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
            self.dates["deadline"] = datetime.ctime(deadline_object)
            
        elif self.formatter == "day": 
            deadline =  start_date + timedelta(days = self.deadline )
            
            deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
            self.dates["deadline"] = datetime.ctime(deadline_object)

        elif self.formatter == "week": 
            deadline =  start_date + timedelta(week = self.deadline )

            deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
            self.dates["deadline"] = datetime.ctime(deadline_object)
            pass

    
    def date_maker(self):
        now = datetime.now()
        self.dates["start date"] = datetime.ctime(now)

        # self.deadline_maker()
     



x = todo_repo("ggd",2,"day")
x.date_maker()
print(x.dates)

x.deadline_maker()
print(x.dates)



