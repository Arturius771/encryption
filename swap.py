import re

def swap(message_content: str):
    previous_message = message_content
    while(True):
      print(f"\n=================\n{previous_message}\n=================\n")

      [target_character, new_character] = prompt_user()

      previous_message = previous_message.replace(target_character,new_character)

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