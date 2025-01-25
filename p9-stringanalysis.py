import string

def get_string():
  return input("Enter the string: ")

def analysis(input_string):
  vowels_count, consonants_count, digits_count, special_chars_count = 0, 0, 0, 0
  special_characters = string.punctuation

  for char in input_string:
    if char in ['a', 'e', 'i', 'o', 'u']:
      vowels_count += 1
    elif char.isdigit():
      digits_count += 1
    elif char in special_characters:
      special_chars_count += 1
    elif char.isalpha():
      consonants_count += 1

  return vowels_count, consonants_count, digits_count, special_chars_count

def display_analysis(input_string):
  vowels_count, consonants_count, digits_count, special_chars_count = analysis(input_string)
  print('The number of vowels in the string:', vowels_count)
  print('The number of consonants in the string:', consonants_count)
  print('The number of digits in the string:', digits_count)
  print('The number of special characters in the string:', special_chars_count)

def display_reversed_string(input_string):
  print('The reversed string is', input_string[::-1])

def main():
  input_string = get_string()
  display_analysis(input_string)
  display_reversed_string(input_string)

main()
