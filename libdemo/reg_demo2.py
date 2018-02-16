
import re


# lst = re.split("[\d,-]+","abc12bbc34zyz,bbc-pqr")

lst = re.findall(" [\d]+","abc12 bbc34 zyz,bbc-pqr 8228 3343")
print(lst)






