
from restcountries import RestCountryApiV2 as rc

# for c in rc.get_countries_by_name("india"):
#     print(type(c))
#     print(dir(c))

for c in  rc.get_all():
    print(c.name, ' - ' ,  c.capital)






