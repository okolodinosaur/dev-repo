'''
while True:
    enter = input("if sign in press 1/ if registration press 0 : ")
    if enter == "0":
        print("registration")
        login = input("login: ")
        password = input("password: ")
        break
    else:
        print("try again")




users = {login : password}


print("sign in....")

while True:
    user_login = input("login: ")
    user_password = input("password: ")
    if user_login == login and user_password == password:
        print("welcome")
        break
    else:
        print("try again")
'''

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
            print(i["title"],i["content"],i["status"])
    if action == "delete":
        for i,note in enumerate(notes):
            print(note,i)
        try:
            value = int(input("what delete: "))
            if 0 <= value <= len(notes)-1:
                notes.pop(value)
            else:
                print("ne tot index")
        except ValueError:
            print("string")
    if action == "edit":
        for i, note in enumerate(notes):
            print(note,i)
        try:
            value = int(input("what edit: "))
            if 0 <= value <= len(notes)-1:
                pass
            else:
                print("ne tot index")
                continue
        except ValueError:
            print("string")
            continue
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