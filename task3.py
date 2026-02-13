file_name = input("Enter the file name : ")

try :
    with open("file_name","r") as file:
        content = file.read()
        print(content)
        
        
        
        
except FileNotFoundError:
       print(f"Oops! the named {file_name} does'not exists")