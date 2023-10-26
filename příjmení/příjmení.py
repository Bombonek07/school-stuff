my_dict = {}

with open('05.in', 'r') as file:
   lines = file.readlines()

for x in lines:
    line = x.replace("\n", "")
    name = line
    if name not in my_dict:
        my_dict[name] = 1
    else:
        my_dict[name] += 1

f = open("prijmeni.txt", "w")
f.write(max(my_dict, key=my_dict.get))
f.write(" ")
f.write(str(max(my_dict.values())))
f.close()