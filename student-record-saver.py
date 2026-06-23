
f1=open("f2.py","w+")
l=['NAME','AGE','BRANCH','CGPA']
for i in range(4):
    f1.write(f"{l[i]}: {input(f"enter your {l[i]}: ")}\n")
f1.seek(0)
print(f1.read())
f1.close()
