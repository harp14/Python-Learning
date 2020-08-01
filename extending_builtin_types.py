# You can extend built-in functions such as str (string); as you can see below I have added an additional
# method called duplicate which can be called when creating an instance of a text object


class Text(str):
    def duplicate(self):
        return self + self


class TrackableList(list):
    def append(self, object):
        print("Append called")
        # Calls the append method from the super class (base class, in this case: list)
        super().append(object)


text = Text("Python")
print(text.duplicate())

list = TrackableList()
list.append("1")
