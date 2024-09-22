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

#* this function makes secret todo folder and makes todo json files in his created folder 

def json_files_maker(path):
    #* got the folder path
    folder_path = f"{path}/todo_lists"

    #* this capsule function makse json files and write "[]" in json files
    def files():    
        os.chdir(folder_path)
        
        with open(folder_path + "/todo_list.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")
        with open(folder_path + "/uncompleted_todos.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")
        with open(folder_path + "/completed_todos.json" , "w" , encoding= "utf-8") as file: 
            file.write("[]")

    #* control of the folder
    if os.path.exists("todo_lists"):
        pass
    else: #* makes secret folder if there is not folder  
        os.mkdir("todo_lists")
        os.system(f"attrib +h {'todo_lists'}")
        files() 
json_files_maker(local_path)

class todo_repo:
    def __init__(self,task:str ,deadline: dict):
        """
        task : a str param. data about task
        deadline: this param should be a dicti. this dicti should has four data. 
            {"minute": -minute number- , "hour": -hour number- , "day": -day number- , "week": -week number-}
        """
        self.work = task
        self.deadline = deadline 
        self.dates = {"start date": None , "deadline": None , "finish date" : None}
    
    def deadline_maker(self):
        #* start date got beacouse deadline will calculate on start date
        deadline = datetime.strptime(self.dates["start date"], "%c")
        
        #*this for loop gets date datas (minute, hours, days and weeks) and calculates deadline
        for key,value in self.deadline.items():

            if key == "minute": 
                #* deadline item added to start date so calculated the deadline
                deadline += timedelta(minutes = value )
                
                #* timedelta object changed to datetime object  
                deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
                self.dates["deadline"] = datetime.ctime(deadline_object)
            
            elif key == "hour":
                deadline += timedelta(hours = value )
                
                deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
                self.dates["deadline"] = datetime.ctime(deadline_object)
                
            elif key == "day": 
                deadline += timedelta(days = value )
                
                deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
                self.dates["deadline"] = datetime.ctime(deadline_object)

            elif key == "week": 
                deadline += timedelta(weeks = value )

                deadline_object = datetime.strptime(str(deadline) , "%Y-%m-%d %H:%M:%S")
                self.dates["deadline"] = datetime.ctime(deadline_object)

    #* creates start date of tasks
    def date_maker(self):
        now = datetime.now()
        self.dates["start date"] = datetime.ctime(now)

x = todo_repo("dwsıjhdc",{"minute" : 10,"hour": 7,"day": 1,"week": 1})
x.date_maker()

x.deadline_maker()


