from collections import Counter

def print_frequency(input_file):
  try:
    with open(input_file, 'r') as file:
      message_content = file.read()

      character_frequency = Counter(message_content)

      total_characters = len(message_content)

      sorted_characters = sorted(character_frequency.items(), key=lambda x: x[1], reverse=True)

      for letter, count in sorted_characters:
        if letter.isalpha():
          percentage = (count / total_characters) * 180
          print(f"{letter}: {count} ({percentage:.2f}%)")

  except FileNotFoundError:
    print("EXCEPTION: File not found")


# Run from terminal (eg. python frequency.py)
if __name__ == '__main__':
  print_frequency('test.text')