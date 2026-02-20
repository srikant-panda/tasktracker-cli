from .database  import Task_database as TD
from . import task_entities_config as tec

db = TD()
c = db.save_And_reload()
def add_task(description):
    db.reload()
    task = {
        "id"          : tec.generate_id(db.tasks),
        'description' : description,
        'status'      : "todo",
        "created at"  : str(tec.get_datetime()),
        "updated at"  : str(tec.get_datetime())
    }
    db.tasks.append(task)
    db.save()
    return task
def list_tasks(status):
    if status == "todo":
        return [target for target in db.tasks if target["status"] == "todo"]
    elif status == "in-progress":
        return [target for target in db.tasks if target["status"] == "in-progress"]
    elif status == 'done':
        return [target for target in db.tasks if target["status"] == "done"]
    else:
        return [target for target in db.tasks]

def update_task(id,updated_description):
    for task in db.tasks:
        if task["id"] == id:
            task["description"] = updated_description
            print("Task updated.")
            return task
    print("Task not found")

def delete_task(id):
    target = [target for target in db.tasks if target['id'] == id or target['id'] > id]
    """_____to delete a task____"""
    if len(target) == 0:
        print(f"Task of {id} not found.")
        return db.save_And_reload()
    db.tasks.pop(0)
    '''_____readjust the indexes_____'''
    if len(target) == 0:
        pass
    else:
        for i in target:
            i['id'] -= 1
    print("Task deleted.")
    return db.save_And_reload()
    
def mark_task(id,status):
    for task in db.tasks:
        if task['id'] == id:
            if task["status"] == status:
                print(f"Task already marked as \"{status}\" ")
            else:
                task["status"] = status
                print(f"Task updated.")
            return db.save_And_reload()

if __name__ == '__main__':
    mark_task(1,'dono')
    pass