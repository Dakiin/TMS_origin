import csv
import json

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["", "person1", "person2", "person3", "person4", "person5"])
    with open("d_file.json") as file1:
        dic = json.load(file1)
        print(dic)
        writer.writerow(["id", *dic.keys()])
        value = dic.values()
        writer.writerow(['name', *[i[0] for i in value]])
        writer.writerow(['age', *[i[1] for i in value]])
