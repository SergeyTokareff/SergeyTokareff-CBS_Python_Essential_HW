class Editor:
    def view_document(self):
        print(f"Перегляд документа.")

    def edit_document(self):
        print(f"Редагування документів недоступне для безкоштовної версії.")

class ProEditor(Editor):
    def edit_document(self):
        print("Редагування документа.")

valid_license_key = "PRO"

license_key = input("Введіть ліцензійний ключ: ")