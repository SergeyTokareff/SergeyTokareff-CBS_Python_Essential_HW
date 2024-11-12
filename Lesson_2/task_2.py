class GraphicObject:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
    

class Rectangle:
    def __init__(self, color="black"):
        self.color = color

class Button(GraphicObject):
    def __init__(self, width: int, height: int, color="blue"):  
        super().__init__(width, height)      
        self.color = color

    def on_click(self):
        print(f"Кнопка  була натиснута.")

button = Button(width=40, height=20)

button.on_click()