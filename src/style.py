from tabulate import tabulate
from .database import Task_database as TD


def style_table(data=None):
    try:
        if data is None:
            data = TD().tasks
        if len(data) == 0:
               print('No task added!')
        else:
                if not isinstance(data,list):
                        print(data)
                        data = [data]
                print(tabulate(data, headers='keys', tablefmt="fancy_grid"))
    except TypeError as e:
          return str(e)