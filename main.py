r = open("data.txt", "r")
temp = r.readline()
pos = int(temp)
r.close()

banner = open("banner.txt", "r")
banner.read(pos)
character = banner.read(1)

if character == "1":
    print("x", end='')

banner.close()


w = open("data.txt", "w")
if pos >= 342:
    pos = -1
w.write(str(pos + 1))
w.close()
