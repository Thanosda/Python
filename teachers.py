class teacher:
    def __init__(self,name,regno):
        self.name=name
        self.regno=regno
    def display(self):
        print(self.name)
        print(self.regno)

hello=teacher("jully",23)
hekk=teacher("kully",65)

hekk.display()

hello.display()