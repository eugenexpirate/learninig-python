import colorgram

colors = colorgram.extract('./day-18/20_001.jpg', 30)

color_list = []

for col in colors:
    rgb = col.rgb
    color_list.append((rgb.r, rgb.g, rgb.b))

print(color_list)

