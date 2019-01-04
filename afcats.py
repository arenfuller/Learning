#working with a list of strings

my_cats=["cameron", "Milo", "Elyshia"]

print("cats in reverse order", my_cats[::1])
print("number of cats", len(my_cats))
print("sorted cats", sorted(my_cats))
print("reverse sorted cats", sorted (my_cats, reverse=True))
print ("1st cat", my_cats[0])

#Add a new cat and see it
my_cats.append("Lex")
print("cats", my_cats)

#remove a cat by name and see the change
my_cats.remove("cameron")
print("cats", my_cats)

#remove cat by its position
del(my_cats[0])
print("cats", my_cats)

print ("Lex" in my_cats)
