"""
145, 
Villa Anandam, 
Meerut Road Industrial Area, 
Ghaziabad, 
201003, 
Uttar Pradesh, 
India

"""

address = "145, villa anandam, meerut road industrial area, ghaziabad, 201003, Uttar Pradesh, India"

hn = address[0:3]
building = address[5:18]
area = address[20:47]
city = address[49:58]

print("H.No.",hn.title())
print("Building:",building.title())
print("Area:",area.title())
print("City:",city.title())