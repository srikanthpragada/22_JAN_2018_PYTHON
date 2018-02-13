
try:
    with open('names.txt','r') as f:
        with open('sorted_names.txt','w') as tf:
            lines = set()
            for line in f.readlines():
                lines.add(line)
            tf.writelines(sorted(lines))
except  OSError as ex:
    print("Sorry! Error : ", ex)


