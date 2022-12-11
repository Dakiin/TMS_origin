s = b'r\xc3\xa9sum\xc3\xa9'
s1 = s.decode()
print(s1)
s2 = s1.encode("Latin1")
print(s2)
s2.decode("Latin1")
print(s2)
