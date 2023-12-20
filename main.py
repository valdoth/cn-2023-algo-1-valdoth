enfants = {
    "Alice": ["Chocolat", "Guimauve"],
    "Bob": ["Caramel", "Fruits"],
    "Charlie": ["Chocolat", "Caramel"],
}
bonbons = {"Chocolat": 10, "Caramel": 8, "Guimauve": 5, "Fruits": 6}

transpose_enfants = {}
for k, v in enfants.items():
  for i in v:
    if i in transpose_enfants.keys():
      transpose_enfants[i].append(k)
    else: 
      transpose_enfants[i] = [k]

result = {}

for k, v in transpose_enfants.items():
  child_part = bonbons[k] // len(v)
  if child_part == 0:
    child_part = 1
  for i in v:
    if i in result.keys():
      result[i].append([k, child_part])
    else: 
      result[i] = [[k, child_part]]

for k, v in result.items():
  print(k, ":", *v)