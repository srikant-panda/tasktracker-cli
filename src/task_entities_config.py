import datetime,time

def generate_id(task):
    if not task:
        return 1
    else:
        return max(task_item['id'] for task_item in task)+1
def get_datetime(request = 'datetime'):
    if request == 'datetime':
        return datetime.datetime.now().replace(microsecond=0)
    elif request == 'date':
        return datetime.date.today()
    elif request == 'time':
        return datetime.datetime.now().time().replace(microsecond=0)