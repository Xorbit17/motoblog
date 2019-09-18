ex_list = ["Dennis", 12]  # MUTABLE!! #Dit heeft een kost

ex_list[0] = "Pommetje horlepiep"
ex_list.append("Kakadee")


ex_tuple = (12, "Lolz")  # IMMUTABLE  #Dit is efficient met geheugen

ex_dict = {"key_1": 12, "key_2": ("Kaka", "Dee")}  # MUTABLE Nog een hogere kost dan een list, maar niet veel
ex_dict_idem = dict(key_1=12,key_2=("Kaka", "Dee"))  # Zelfde
# Alles kan dienen als key, zolang immutable

import json  # Heel snel

var_dict = json.loads("{\"key_1\": 12, \"key_2\":30}")

