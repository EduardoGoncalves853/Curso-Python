
#* Boolean True or False
name = "Eduardo"
age = 31
is_admin = True 

print(is_admin)
print(type(is_admin))
#_____________________

#* Structural Types (Collections)
animes = ["Dragon ball","One Punch Man", "Baki", "Zom 100", "Mob psycho 100"]
            # => 0            1            2         3             4
            # =>-5           -4           -3        -2            -1
print(animes)
print("___________________________")
print(f" posição  0 : {animes[0]}")
print(f" posição  1 : {animes[1]}")
print(f" posição -2 : {animes[-2]}")

#_____________________

# Array dentro de array ↓
list = ["A", 123, True, ["B", "C"]]
    # => 0    1    2      3    4
# ↓ Modifica o array
list[2] = False

print(list[3][0])
print(list)

# tuple
# +são imutáveis
tuple = ("A", 123, True)

print(type(tuple))
print(tuple[1])

# tuple[1]= 798  #! error: tuple is immutable
print(tuple)

#dict
user = {
    "name": "Emanuel",
    "age": 31,
    "is_admin": True,
}

print(user)
print("___________________________")
print(type(user["name"])) #str
print(type(user["age"])) #Number
print(type(user["is_admin"])) #Boolean
print("___________________________")
print(user["name"])
print(user["age"])
print(user["is_admin"])