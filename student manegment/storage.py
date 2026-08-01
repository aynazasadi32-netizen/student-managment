with open("database/students.json" , 'r+') as f:
    print(f.read())
    f.write("\nhellow matin")
    print(f.read())
    f.close()
