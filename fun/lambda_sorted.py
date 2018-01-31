def length(s):
    return len(s)

def last_name(s):
    return s.split()[-1]


names = ['Bill Gates','Larray Ellison','Micheal Dell','Jeff Bezzos','Larry Page','Steve Jobs']

# for n in sorted(names):
#     print(n)
#
# for n in sorted(names,key=length):
#     print(n)

# for n in sorted(names,key=last_name):
#     print(n)

for n in sorted(names,key = lambda n: n.split()[-1]):
    print(n)

