import pickle

f = open("employees.dat","rb")
employees = pickle.load(f)  # De-serialization

for dept ,emps in employees.items():
    print(dept ,",".join(sorted(emps)))