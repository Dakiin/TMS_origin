s1 = "Hello\n"
s2 = "My\n"
s3 = "Best\n"
s4 = "Friend"

with open("test.txt", "w", encoding="utf-8") as file:
    file.write(s1)
    file.write(s2)

with open("test.txt", "a", encoding="utf-8") as file:
    file.write(s3)
    file.write(s4)
