##Write the code that will take a string and make this conversion given a number of rows

def zigzag(s,rows):
  assert rows > 0
  if rows == 1:
    return s
  temp = [[] for _ in range(rows)]
  position = 0
  direction = 1
  for char in s:
    temp[position].append(char)
    if position == 0:
      direction = 1
    elif position == rows-1:
      direction = -1
    position += direction
  return ''.join([''.join(row) for row in temp])
