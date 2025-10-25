import random
import string

# Used to create a randomly shuffled message.

def substitution(message_content):
    characters = list(string.ascii_letters)
    shuffled = list(characters)
    random.shuffle(shuffled)
    substitution_dict = dict(zip(characters, shuffled))
    encrypted_message = ''.join(substitution_dict.get(char, char) for char in message_content)
    
    print(encrypted_message)
    
# Run from terminal (eg. >python frequency.py)
if __name__ == '__main__':
  print("What file do you want to analyse?")
  filepath = input()

  try:
    with open(filepath, 'r') as file:
      message_content = file.read()

      substitution(message_content)

  except FileNotFoundError:
    print("EXCEPTION: File not found")