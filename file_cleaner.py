f = open('movie_names.txt').readlines()

l = []
for line in f:
  if line[0].isdecimal():
    l.append(line.strip('1234567890 \n'))
  elif line.startswith('Columns'):
    l += line[11:-2].split(', ')

#print('\n'.join(l))

textfile = open("movie_names_2.txt", "w")#this is our final file
for element in l:
    textfile.write(str(element) + "\n")
textfile.close()
