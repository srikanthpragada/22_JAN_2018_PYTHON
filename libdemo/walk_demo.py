import os

allfiles = os.walk(r"e:\classroom\python\jan22\demo")

for (dirname, directories, files) in allfiles:
    # print directory name
    print("Directory : ", dirname)
    print("=============" + "=" * len(dirname))
    # print files in that directory
    for file in files:
        print(file)
