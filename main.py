def show_note(note : dict, idx : int):
    title = note["title"][:14].ljust(14)
    content = note["content"][:50].ljust(50)
    temp_status = note["status"].ljust(8)
    print(f"    {idx:<2}    | {title} | {content} | {temp_status} |")

def show_header():
    print("############################################################################################")
    print("# INDEX ###    TITLE    ###                    CONTENT                       ### STATUS    #")
    print("############################################################################################")

def delete_note_by_index(notes : list[dict],i:int):
    if 0 <= i <= len(notes)-1:
        notes.pop(i)



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

notes : list[dict] = []
status = {1: "Complete", 2: "Progress", 3: "Backlog", 4: "Waiting"}


while True:
    action = input("add/delete/edit/show: ")
    if action == "add":
        print("Type note name (up to 14 symbols)")
        note_title = input()
        if len(note_title) > 14:
            print("Too long name")
            continue
        print("Type note content (up to 50 symbols)")
        note_content = input("content: ")
        if len(note_content) > 50:
            print("Too long content")
            continue
        print("choose note's status...")
        for key, value in status.items():
                print(key, " ", value)
        try:
            note_status_input = int(input())
        except ValueError:
            continue    
        note_status = status.get(note_status_input)
        note = {"title": note_title, "content": note_content, "status": note_status}
        notes.append(note)
    elif action == "exit":
        break
    elif action == "show":
        show_header()
        for idx, note in enumerate(notes):
            show_note(note,idx)
    elif action == "delete":
        show_header()
        for i,note in enumerate(notes):
            show_note(note,i)
        try:
            value = int(input("what delete: "))
        except ValueError:
            print("index out of range")
            continue
        delete_note_by_index(notes,value)
    elif action == "edit":
        for i, note in enumerate(notes):
            print(note,i)
        try:
            value = int(input("what edit: "))
        except ValueError:
            continue
        if 0 <= value <= len(notes)-1:
            pass
        else:
            print("ne tot index")
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
    else:
        print("Wrong command...\nTry again")