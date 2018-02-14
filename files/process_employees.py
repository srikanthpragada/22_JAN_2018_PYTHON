import pickle

try:
    with open('employees.txt','r') as f:
        employees = {}
        for line in f.readlines():
            parts = line.split(',')
            if len(parts) == 2:
                dept = parts[0]
                emp = parts[1].strip("\n")
                if dept in employees:
                    employees[dept].add(emp)
                else:
                    emps  = set()
                    emps.add(emp)
                    employees[dept] = emps

    # save employees to employees.dat
    tf = open('employees.dat','wb')
    pickle.dump(employees,tf)  # Serialization
    tf.close()
    print("Saved Employees to Employees.Dat")

    for dept,emps in employees.items():
         print(dept,",".join(sorted(emps)))
except:
    print("File not found!")
