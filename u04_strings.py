paragraph='''hello there.
Using three' we can write like a paragraph.'''
print(paragraph)
print(paragraph[-2])
print("using [-2] will print string from the reverse(-1 is last)")
print(paragraph[0:6])
print("using [0:6] will print string from index value 0 to 5,not 6")
print(paragraph[5:])
print("using [5:] will print string from index value 5 to end")
print(paragraph[:8])
print("using [:8] will print string from index value 0 to 8")
another=paragraph[:]
print("using another=paragraph[:] will let you copy entire string to another")
name='Jennifer'
print(name[1:-1])
