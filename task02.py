activities = "Dasturlash, Sun’iy intellekt, Web dizayn"
cleaned = activities.lower().replace("’", "'").split(", ")
snake_case = "_".join(word.replace(" ", "_") for word in cleaned)
print(snake_case)

