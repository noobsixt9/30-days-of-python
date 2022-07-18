alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(message, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for letter in message:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift_amount
      new_message = alphabet[new_position]
      end_text += new_message
    else:
      end_text += letter
  print(f"Your {cipher_direction}d message is {end_text}")
    
    
from art import logo
print(logo)
end_program = False
while not end_program:
  direction = input("Enter 'decode to decrypt and 'encode' to encrypt.\n")
  text = input("Enter text message:\n")
  shift = int(input("Enter shift number:\n"))
  shift = shift % 26
  caesar(message=text, shift_amount=shift, cipher_direction=direction)
  restart = input("Try again(yes/no)\n")
  if restart == "no":
    end_program = True
    print("GoodBye!")
