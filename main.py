while True:
    enter = input("if sin in press 1/ if registration press 0 : ")
    if enter == "0":
        print("registration")
        login = input("login: ")
        password = input("password: ")
        break
    else:
        print("try again")


# jopa)))

users = {login : password}

print("sing in....")

while True:
    if input("login: ") == login and input("password: ") == password:
        print("welcome")
        break
    else:
        print("try again")

notes : list[dict] = []

while True:
    action = input("add/delete/edit/show: ")
    if action == "add":
        note_title = input("title: ")
        note_content = input("content: ")
        note_status = input("status: ")
        note = {"title": note_title, "content": note_content, "status": note_status}
        notes.append(note)
    if action == "exit":
        break
    if action == "show":
        for i in notes:
            print(i)
    if action == "delete":
        for note, i in enumerate(notes):
            print(note,i)
        value = int(input("what delete: "))
        notes.pop(value)
    if action == "edit":
        for i, note in enumerate(notes):
            print(i,note)
        value = int(input("what edit: "))
        choise = input("title/content/status or all: ")
        if choise == "title":
            notes[value]["title"] = input("title: ")
        if choise == "content":
            notes[value]["content"] = input("content: ")
        if choise == "content":
            notes[value]["status"] = input("status: ")
        if choise == "all":
            notes[value]["title"] = input("title: ")
            notes[value]["content"] = input("content: ")
            notes[value]["status"] = input("status: ")