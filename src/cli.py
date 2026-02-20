import argparse

# parser = argparse.ArgumentParser(prog='task',description="Process a variable number of input files.")




'''_________add task argument_______'''
parser = argparse.ArgumentParser(prog='task')

subparser = parser.add_subparsers(dest="command",required=True)

add_parser = subparser.add_parser('add')
add_parser.add_argument(
    'description', 
    nargs='+',  # Accepts one or more arguments
    type=str,
    help="Write one or more tasks (use quotes for multi-word tasks)"
)

'''__________list task argument________'''

list_parser = subparser.add_parser('list',help="Used for list the tasks (default=all)")
list_parser.add_argument(
    "type",
    nargs="?",
    choices=["todo","in-progress","done"],
    default="All",
    type=str,
    help="Choose one for filter the list"
)

'''_________mark parser__________'''
mark_parser = subparser.add_parser('mark-in-progress',help="mark tas as in-progress")
mark_parser.add_argument('id',help='required an id to modify the state.')
mark_parser = subparser.add_parser('mark-todo',help="mark tas as todo")
mark_parser.add_argument('id',help='required an id to modify the state.')
mark_parser = subparser.add_parser('mark-done',help="mark tas as done")
mark_parser.add_argument('id',help='required an id to modify the state.')
update_parser = subparser.add_parser('update',help="update the task")
update_parser.add_argument('id',help='requires an id for update')
update_parser.add_argument('updated_description',help='requires a new description to update the task.')
delete_parser = subparser.add_parser('delete',help="delete task")
delete_parser.add_argument('id',type=int,help='require id for delete')

args = parser.parse_args()
c = args.command
if c == 'add':
    a = args.description
elif c == "list":
    l = args.type
elif c == "delete":
    d = args.id
elif c == 'update':
    u1 = args.id
    u2 = args.updated_description
elif c == 'mark-done' or c =='mark-in-progress' or c == 'mark-todo':
    m = args.id

