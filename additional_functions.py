def capitalize_letter(letter):
  if letter == 'a': return 'A'
  if letter == 'b': return 'B'
  if letter == 'c': return 'C'
  if letter == 'd': return 'D'
  if letter == 'e': return 'E'
  if letter == 'f': return 'F'
  if letter == 'g': return 'G'
  if letter == 'h': return 'H'
  if letter == 'i': return 'I'
  if letter == 'j': return 'J'
  if letter == 'k': return 'K'
  if letter == 'l': return 'L'
  if letter == 'm': return 'M'
  if letter == 'n': return 'N'
  if letter == 'o': return 'O'
  if letter == 'p': return 'P'
  if letter == 'q': return 'Q'
  if letter == 'r': return 'R'
  if letter == 's': return 'S'
  if letter == 't': return 'T'
  if letter == 'u': return 'U'
  if letter == 'v': return 'V'
  if letter == 'w': return 'W'
  if letter == 'x': return 'X'
  if letter == 'y': return 'Y'
  if letter == 'z': return 'Z'
  return letter

def capitalize(inp_string):
  output = ''
  for letter in inp_string:
    output += capitalize_letter(letter)
  return output
