dict_comp={x**2 for x in range(4)}
print(dict_comp)

book = {
	'title': 'The 48 Laws of Power',
	'author': 'Robert Greene',
	'date_ published': 1998,
	'in_stock': True
}

print(book)

dict_comp={x for x in book.items()}
print(dict_comp)
data = ("george", "localman", "honen", "smallgod")
name , *_ = data
print(name)
