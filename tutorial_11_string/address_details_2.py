"""
145, 
Villa Anandam, 
Meerut Road Industrial Area, 
Ghaziabad, 
201003, 
Uttar Pradesh, 
India

"""

address = "145, villa anandam square, meerut road industrial area, ghaziabad, 201003, Uttar Pradesh, India"

list = address.split(",")
print(list)
print(type(list))
hn = list[0].strip()
building = list[1].strip()
area = list[2].strip()
city= list[3].strip()


print("H.No.",hn.title())
print("Building:",building.title())
print("Area:",area.title())
print("City:",city.title())