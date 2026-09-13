name = ["keanu reeves,", " denji,", " moistcritical,"]
print(name[0].title() + name[1].title() + name[2].title() + " you are all invited to dinner!")
print("Unfortunately, " + name[0].title() + " can't make it to the dinner!")
name[0] = "maynard keenan,"
print(name[0].title() + name[1].title() + name[2].title() + " you are all invited to dinner!")
print("Good news! I found a bigger dinner table, so I can invite more guests!")
name.insert(0, "mac demarco, ")
name.insert(2, " kurt cobain,")
name.append(" steven universe,")
print(name[0].title() + name[1].title() + name[2].title() + name[3].title() + name[4].title() + name[5].title() + " you are all invited to dinner!")