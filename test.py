
#with as statement
with open('file.txt', 'w') as file:
    file.write('Hello world!')

# better than

file = open('file.txt' , 'w')
try:
    file.write('hello world!')
finally:
    file.close()