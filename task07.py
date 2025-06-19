data = "Ism:Ali, Familiya:Valiyev, Yil:2002"
for part in data.split(", "):
    key, value = part.split(":")
    print(f"{key}: {value}")

