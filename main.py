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


def add_note(notes, status):
    print("Type note name (up to 14 symbols)")
    note_title = input()
    if len(note_title) > 14:
        print("Too long name")
        return
    print("Type note content (up to 50 symbols)")
    note_content = input("content: ")
    if len(note_content) > 50:
        print("Too long content")
        return
    print("choose note's status...")
    for key, value in status.items():
            print(key, " ", value)
    try:
        note_status_input = int(input())
    except ValueError:
        return    
    note_status = status.get(note_status_input)
    note = {"title": note_title, "content": note_content, "status": note_status}
    notes.append(note)        


def edit_note(notes):
    for i, note in enumerate(notes):
        print(note,i)
    try:
        value = int(input("what edit: "))
    except ValueError:
        return
    if 0 <= value <= len(notes)-1:
        pass
    else:
        print("ne tot index")
        return
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
        

def main():
    while True:
        action = input("Type add/edit/print\n")
        if action == "add":
            add_note(notes, status)
        elif action == "edit":
            edit_note(notes)
        elif action == "print":
             print(notes)


main()