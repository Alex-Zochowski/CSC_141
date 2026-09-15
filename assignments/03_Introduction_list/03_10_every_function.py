random = ["Mount Fuji", "Nile River", "Italy", "New York City", "German"]
print(random)
print(random[3])
random.remove("Italy")
print(sorted(random))
random.reverse()
random[2] = "apple"
print(random)
random.reverse()
print(sorted(random, reverse=True))
random.insert(2, "Italy")
length = len(random)
print(length)