#1
x = 10
y = 20
print(x + y)

#2
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)
print(my_list_len)
print(my_list[-1])


#3
my_string = 'hello world'
print(my_string.upper())

#4
z = ['a', 'b', 'c']
z.append('d')
print(z)

#5
x = 10
print(x)
y = 20
print(x * y)

#6
color = 'My favorite color is {}, what is yours?'.format('blue')
print(color)

#7 make the entries in this list unique
schools = {'harris', 'booth', 'crown', 'harris', 'harris'}
print(set(schools))

#8 change the 'dog' entry to 'cat'
animals = ['bird', 'horse', 'dog', 'fish']
animals[2] = 'cat'
print(animals)

#9 make this string take a name based on a variable (you can modify the code on this one)
name = 'Sarah'
welcome = f'Hello {name}, and welcome to Data and Programming!'
print(welcome)

#10 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'
print(my_sent.lower().split())
