class Verify:


    def __init__(self, driver):
        self.driver = driver

    def ver_user(self,name):
        name = name.split("\n", 1)
        print(name)
        if name[0] != "hari01":
            print("\nwrong")
        else:
            print("\nright")