from .database  import Task_database as TD
# from . import task_entities_config as tec
from .model import TaskModel
from typing import List,Literal,Union,Dict,Any

def add_task(description : List[str]) -> List[Dict[Any,Any]]:
    db = TD()
    db.reload()
    added_tasks : List[Dict[Any,Any]] = []
    for i in description:
        task = TaskModel(description = i)
        added_tasks.append(task.model_dump())
        db.tasks.append(task.model_dump(mode='json'))
    db.save_And_reload()
    # print(task)
    # print(type(task))
    return added_tasks
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
   x = add_task(["Hello bachho"])
   print(x)