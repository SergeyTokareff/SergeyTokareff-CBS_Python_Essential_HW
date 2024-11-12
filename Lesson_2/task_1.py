class Editor:
    def view_document(self):
        print(f"Ми можемо переглядати документ.")

    def edit_document(self):
        print(f"Редагування документів недоступне для безкоштовної версії.")

class ProEditor(Editor):
    def edit_document(self):
        print("Ми можемо редагувати документ.")

valid_password = "PRO12345"

password = input("Введіть пароль: ")

if password == valid_password:
    obj = ProEditor()
else:
    obj = Editor()    

obj.view_document()
obj.edit_document()