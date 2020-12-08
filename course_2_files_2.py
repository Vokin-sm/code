import os

os.chdir("main")
con = []
for root, dirs, files in os.walk("main"):
    for file in files:
        if file.endswith(".py"):
            con.append(root)
            break
print(con)
with open("dirs.txt", "w") as d:
    d.write("\n".join(con))
print(os.getcwd())