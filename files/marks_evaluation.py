try:
    with open('marks.txt', 'r') as f:
        count = 0
        for line in f.readlines():
            if len(line.strip()) == 0:   # blank line so skip
                continue

            marks = line.split(',')
            for m in marks:
                try:
                    if int(m) < 50:
                        break    # student failed
                except:
                    break   # marks not available, means fail
            else:
                count += 1

        print("No. of student passed : ", count)
except Exception as ex:
    print("Error : ", ex)
