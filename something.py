file = open("24.txt")
string = file.readline().strip()

MIN = 10 * 100
for i in range(len(string)):
    if string[i] == "D":
        for j in range(i + 1, len(string)):
            if string[j] == "D":
                if MIN > j - i - 1 and len(string[i:j-i]) != 2:
                    MIN = j - i - 1
print(MIN)