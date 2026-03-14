from src import TO, parse_args, style


def main() -> int :
    args = parse_args()

    if args.command == "add":
        try:
            result = TO.add_task(args.description)
            if type(result) == str:
                print(result)
                return 1
            else:
                print("------------------------------added task---------------------------------------")
                style.style_table(result)
                return 0
        except Exception as e:
            print(str(e))

    if args.command == "update":
        result = TO.update_task(args.id, args.description)
        if result is None:
            print("Task not found.")
            return 1
        style.style_table(result)
        return 0

    if args.command == "delete":
        result = TO.delete_task(args.id)
        print("-----------------------------current task--------------------------------------")
        style.style_table(result)
        return 0

    if args.command == "list":
        result = TO.list_tasks(args.type)
        style.style_table(result)
        return 0

    if args.command == "mark-in-progress":
        changed = TO.mark_task(id=args.id, status="in-progress")
        return 0 if changed is not None else 1

    if args.command == "mark-done":
        changed = TO.mark_task(id=args.id, status="done")
        return 0 if changed is not None else 1

    if args.command == "mark-todo":
        changed = TO.mark_task(id=args.id, status="todo")
        return 0 if changed is not None else 1

    return 1


if __name__ == "__main__":
    raise SystemExit(main())