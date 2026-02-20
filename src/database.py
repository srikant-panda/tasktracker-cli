'''_____________Databse storage management_____________'''
import os
import json



class Task_database:
    def __init__(self):
        self.filepath = os.path.join(os.path.dirname(__file__),'storage','task.json')
    
        try:
            if os.path.exists(self.filepath):
                with open(self.filepath,'r') as f:
                    self.tasks= json.load(f)

            else:
                self.tasks= []
                with open(self.filepath,'w+') as f:
                    json.dump(self.tasks,f,indent=4)
        except Exception as e:
            os.rename(self.filepath,f'{self.filepath}.bak')
            self.tasks= []
            with open(self.filepath,'w') as f:
                json.dump(self.tasks,f,indent=4)

    def save(self):
        with open(self.filepath,'w') as f:
            # f.write('[]')
            json.dump(self.tasks,f,indent=4)
    def reload(self):
        with open(self.filepath,'r') as f:
            # print(self.tasks,'hello')
            self.tasks = json.load(f)
            return self.tasks    
    def save_And_reload(self):
        self.save()
        self.reload()
        return self.tasks
'''____________________________End of database.py___________________________'''

if __name__ == "__main__":       # If this module is imported then It becomes the name of the class, not the name of the file. It is because we are importing the class instead of __main__ whch is defailt namre of a file. So if in the imported module contain any if case eith this that fail. It will not execute because the name of the file is not __main__ but the name of the class. So it is important to understand the difference between importing a class and importing a file. If we import a file, then the name of the file will be __main__. But if we import a class, then the name of the class will be the name of the module. So it is important to understand this difference when we are importing modules in Python. best for keeping test cses.
    u1 = Task_database()
    # print(u1.filepath)