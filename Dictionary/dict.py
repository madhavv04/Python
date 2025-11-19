dic1 = { "car " : { "BMW" : ['M4','M3','M2'],"Audo" : ['M4','M3','M4']}}
print(dic1)
print(dic1["car "]["BMW"])
print(dic1["car "]["Audo"])
print(dic1["car "]["BMW"][1])
print(dic1["car "]["Audo"][2])



car  =  dic1["car "]
print(car)

car_bmw = car["BMW"]

print(car_bmw)
car_bmw_m3 = car_bmw[1]
print(car_bmw_m3)