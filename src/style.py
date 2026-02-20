from tabulate import tabulate
import json
from src.database import Task_database as TD

u1 = TD()

def style_table(data = u1.tasks):
    try:
        if len(data) == 0:
               print('No task added!')
        else:
                if not type(data) == list:
                        data = [data]
                print(tabulate(data, headers='keys', tablefmt="fancy_grid"))
    except TypeError:
          return
if __name__ == "__main__":
    task = {
            'id' : 1,
            'status' : "done",
    }

    style_table(task)