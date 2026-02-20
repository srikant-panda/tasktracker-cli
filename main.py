import src.operations as TO
import src.cli as cli
import src.style as style



def main():
    pass

if cli.c == 'add':
    success = False
    for i in range(len(cli.a)):
        try:
            c = TO.add_task(cli.a[i])
            success = True
        except:
            print("Somethong wrong happend try again!")
    if success:
        print('Task created')
        print('------------------------------added task---------------------------------------')
        style.style_table(c)
elif cli.c == 'update':
    try:
        c = TO.update_task(int(cli.u1),cli.u2)
        style.style_table(c)    
    except:
        print("Somthing wrong happend try again!")
elif cli.c == 'delete':
    success = False
    try:
        c = TO.delete_task(cli.d)
        success = True
    except Exception as e:
            print(e)
    except Exception as e:
            print("Somthing wrong happend try again!",e)
    if success:
        print('-----------------------------current task--------------------------------------')
        style.style_table(c)
elif cli.c == 'list':
    try:
        c = TO.list_tasks(cli.l)
        style.style_table(c)
    except Exception as e:
        print("Somthing wrong happend try again!",e)
elif cli.c == 'mark-in-progress':
    try:
        TO.mark_task(id =int(cli.m),status='in-progress')
    except Exception as e:
        print(e)
elif cli.c == 'mark-done':
    try:
        TO.mark_task(id=int(cli.m),status='done')
    except:
        print("Somthing wrong happend try again!")
elif cli.c == 'mark-todo':
    try:
        TO.mark_task(id=int(cli.m),status='todo')
    except:
        print("Somthing wrong happend try again!")