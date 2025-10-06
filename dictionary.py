dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(set(dict1.keys()) & set(dict2.keys())) 
print(set(dict1.keys()) | set(dict2.keys()))  
print(set(dict1.keys()) - set(dict2.keys()))  


group=dict(name="saniya",age=20,city="kolhapur")
print(group)