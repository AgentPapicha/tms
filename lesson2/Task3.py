x = 5
y = 5
z = 5

print(f"The type of variables x: {type(x)}, y: {type(y)}, z: {type(z)}")
print(f"The id of variables: \n x: {id(x)} \n y: {id(y)} \n z: {id(z)}")

x = str(x)
y = str(y)
z = str(z)

print(f"The type of variables after changes x: {type(x)}, y: {type(y)}, z: {type(z)}")
print(f"The id of variables after changes: \n x: {id(x)} \n y: {id(y)} \n z: {id(z)}")

a = [1]
b = [1]

print(f"The type of variables a: {type(a)}, b: {type(b)}")
print(f"The id of variables: \n a: {id(a)} \n b: {id(b)}")

a = bytes(a)
b = bytes(b)

print(f"The type of variables after changes a: {type(a)}, b: {type(b)}")
print(f"The id of variables after changes: \n a: {id(a)} \n b: {id(b)}")
