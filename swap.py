import re

# Used to decrypt.

def swap(message_content: str):
    character_dict = {}    
    print_message(message_content)
    while(True):            
      # print_message(message_content, 'Original')
      print(character_dict)

      [target_character, new_character] = prompt_user()
      character_dict[target_character] = new_character
      translation_table = str.maketrans(character_dict)      
      translated = message_content.translate(translation_table)

      print_message(translated, 'Translated')
  
def print_message(message, header = ''):
  delimiter = "\n==================================\n"
  print(f"\n{header}:\n{delimiter}{message}{delimiter}")

def prompt_user() -> [str, str]:
  print("Swap character X=Y:")
  command = input()

  if(input_is_valid(command)):
    target_character = command[0]
    new_character = command[2]

    return [target_character, new_character]
  else:
    print("Input did not match pattern, try again")
    return prompt_user()


def input_is_valid(input: str) -> bool:
  if re.compile('[A-z0-9][=][A-z0-9]').match(input):
    return True
  else: 
    return False

# Run from terminal (eg. >python frequency.py)
if __name__ == '__main__':
  print("What file do you want to analyse?")
  filepath = input()

  try:
    with open(filepath, 'r') as file:
      message_content = file.read()

      swap(message_content)

  except FileNotFoundError:
    print("EXCEPTION: File not found")