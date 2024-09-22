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
