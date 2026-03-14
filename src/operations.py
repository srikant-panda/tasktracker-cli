from .database  import Task_database as TD
from .model import TaskModel
from typing import List,Literal,Union,Dict,Any



def add_task(description : str) -> Union[Dict[Any,Any],str]:
    db = TD()
    db.reload()
    if len(description) == 0:
        return "Error : Description should not be empty."
    
    task = TaskModel(description = description)
    db.tasks.append(task.model_dump(mode='json'))
    db.save_And_reload()
  
    return task.model_dump()
    
def list_tasks(status : Literal['todo','in-progress','done']) -> List[Dict[Any,Any]]:
    db = TD()
    if status == "todo":
        return [target for target in db.tasks if target["status"] == "todo"]
    elif status == "in-progress":
        return [target for target in db.tasks if target["status"] == "in-progress"]
    elif status == 'done':
        return [target for target in db.tasks if target["status"] == "done"]
    else:
        return [target for target in db.tasks]

def update_task(id : str,updated_description : str) -> Union[None,dict]:
    db = TD()
    for task in db.tasks:
        if task["id"] == id:
            task["description"] = updated_description
            print("Task updated.")
            return task
    print("Task not found")
    # return ""

def delete_task(id : str) -> List[Dict[Any,Any]]:
    db = TD()
    """_____to delete a task____"""
    if id == "*":
        db.tasks = []
        print("All task deleted.")
        return db.save_And_reload()
    for index , value in enumerate(db.tasks):
        if value['id'] == id:
            db.tasks.pop(index)
            print("Task deleted.")
            return db.save_And_reload()
    return db.save_And_reload()

    
def mark_task(id : str,status : str) -> Union[bool,None]:
    db = TD()
    for task in db.tasks:
        if task['id'] == id:
            if task["status"] == status:
                print(f"Task already marked as \"{status}\" ")
                return False
            task["status"] = status
            print(f"Task updated.")
            db.save_And_reload()
            return True
        
if __name__ == '__main__':
   x = add_task("Hello bachho")
   print(x)