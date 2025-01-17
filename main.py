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
    json_files = [folder_path + "/todo_list.json", folder_path + "/completed_todos.json" , folder_path + "/uncompleted_todos.json"] 
    return json_files
JSON_paths = json_files_maker(local_path)



class todo_repo:

    def __init__(self,work:str ,deadline: dict):
        """
        work : a str param. data about task\n
        deadline: this param should be a dicti. this dicti should has four data. \n
            {"minute": -minute number- , "hour": -hour number- , "day": -day number- , "week": -week number-}\n
        \t there can be one of them or all of them. it is user's choice
        """
        self.work = work
        self.deadline = deadline 
        self.is_it_done = None 
        self.dates = {"start date": None , "deadline": None , "finish date" : None}
        self.error_handing(self.deadline)
    
    #* error_handing function chechs lenght of dictionary becaouse the deadline cant be calculated if the dictionary is empty
    def error_handing(self, dates: dict):
        if len(dates) == 0:
            raise ValueError("dict must include date data ")

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

class todo_saver:
    def __init__(self,object: todo_repo ,paths: list):
        """
            The object parameter is used like a repository.\n
            The paths parameter is needed to access the JSON files.\n        
        """
        #* date and deadline were created using the recived object 
        self.object = object
        self.object.date_maker()
        self.object.deadline_maker()
        
        self.paths = paths
        self.datas = self.data_getter(self.paths)
        #* "timeout controller" function finds uncompleted todo and retrieved them . the retrieved todos are saved to uncompleted_todos.json file  
        for i in range(len(self.datas[0])):    
            self.timeout_controller()
            

    #* this function collect datas from JSON files for Operations 
    def data_getter(self,paths):
        with open(paths[0] , "r+" , encoding="utf-8") as file:
            todo_list = js.load(file)
        
        with open(paths[1] , "r+" , encoding="utf-8") as file:
            completed_todo_list = js.load(file)
        
        with open(paths[2] , "r+" , encoding="utf-8") as file:
            uncompleted_todo_list = js.load(file)
        return [todo_list , completed_todo_list , uncompleted_todo_list]
    
    def save_todo(self):
        self.datas[0].append(self.object.__dict__)
        with open(self.paths[0] , "w" , encoding= "utf-8") as file:
            js.dump(self.datas[0] , file , indent=4 , sort_keys= False)
    
    def read_todo(self,choice: int):
        """
        if the user's choice is 1 ,it will read to-do list JSON file \n
        if the user's choice is 2 ,it will read completed to-do list JSON file\n
        if the user's choice is 3 ,it will read uncompleted to-do list JSON file\n
        """
        if choice == 1:
            todos = self.datas[0]
            for index,todo in enumerate(todos,1):
                print(f"{'*' * 20} {index} {'*' * 20}")
                print(js.dumps(todo,indent=4,sort_keys=False) , end="\n\n")
        elif choice == 2:
            todos = self.datas[1]
            for index,todo in enumerate(todos,1):
                print(f"{'*' * 20} {index} {'*' * 20}")
                print(js.dumps(todo,indent=4,sort_keys=False) , end="\n\n")
        elif choice == 3:
            todos = self.datas[2]
            for index,todo in enumerate(todos,1):
                print(f"{'*' * 20} {index} {'*' * 20}")
                print(js.dumps(todo,indent=4,sort_keys=False) , end="\n\n")

    def delete_todo(self,index):
        todo = self.datas[0][index]
        self.datas[0].remove(todo)
        todo["is_it_done"] = False
        
        self.datas[2].append(todo)
        
        with open(self.paths[0] , "w", encoding="utf-8") as file:
            js.dump(self.datas[0],file, indent=4,sort_keys=False)

        with open(self.paths[2] , "w", encoding="utf-8") as file:
            js.dump(self.datas[2],file, indent=4,sort_keys=False)

    def timeout_controller(self):
        today = datetime.now()
        for index , todo in enumerate(self.datas[0]):
            deadline = todo["dates"]["deadline"]
            deadline = datetime.strptime(deadline,"%c")
            date_difference =  deadline - today
            if date_difference.days < 0:
                self.delete_todo(index=index)
                descp = f"""the "{todo['work']}" has been timed out so it has been added to uncompleted TODO list\nstart date: {todo['dates']['start date']}\ndeadline: {todo['dates']['deadline']}\ntoday: {datetime.ctime(datetime.now())}"""
                print(descp,end="\n\n")
                break
       


x = todo_repo("try",{"day" : 1})

y = todo_saver(x,JSON_paths)
# y.save_todo()
y.read_todo(3)
