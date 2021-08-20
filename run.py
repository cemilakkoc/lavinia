lavinia = open("lavinia.txt", "r").read()
_ = lavinia.split("\n\n")[-1]
print(_)