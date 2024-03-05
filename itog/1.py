a = open("itog/1.txt").readline()
a = a.replace("AB", " ").replace("BA", " ").split(" ")
print(max(map(len, a)))