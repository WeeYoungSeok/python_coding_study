# 저항
dict = {"black" : 0, "brown" : 1, 
        "red" : 2, "orange" : 3,
        "yellow" : 4, "green" : 5, 
        "blue" : 6, "violet" : 7,
        "grey" : 8, "white" : 9}

for i in range(3):
    if i < 2:
        str += str(dict[input()])
    else:
        print(int(str) * (10 ** dict[input()]))


dict = ["black", "brown", 
        "red", "orange",
        "yellow", "green", 
        "blue", "violet",
        "grey", "white"]

string_num = ""
for i in range(3):
    o = input()
    for j in range(len(dict)):
        if dict[j] == o:
            if i < 2:
                string_num += str(j)
                break
            else:
                print(int(string_num) * (10 ** j))
        