alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(text,shift):
#   encode=""
#   for char in text:
#     position = alphabet.index(char)
#     new_position = position + shift
#     new_char = alphabet[new_position]
#     encode += new_char
#   print(encode)
    
    # ascii_char = ord(text[char])
    # if ascii_char != 32:
    #   ascii = ascii_char + shift -1
    #   ascii -= 96
    #   if ascii > 25:
    #     ascii -= 25
    #   encode.append(alphabet[ascii])
      
    # else:
    #   encode.append(" ")
  # print ("".join(encode))
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"
# def decrypt(text,shift):
#   decode=""
#   for char in text:
#     position = alphabet.index(char)
#     new_position = position - shift
#     new_char = alphabet[new_position]
#     decode += new_char
#   print(decode)
# if direction == 'encode':
#   encrypt(text,shift)
# elif direction == 'decode':
#   decrypt(text,shift)

def caesar(text,shift,direction):
  code = ""
  shift = shift % 26
  if direction == 'decode':
      shift *= -1
  for char in text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift
      new_char = alphabet[new_position]
      code += new_char
    else:
      code += char
  print(code)
  #   ascii_char = ord(text[char])
  #   if ascii_char != 32:
  #     ascii = ascii_char - shift -1
  #     ascii -= 96
  #     if ascii < 0:
  #       ascii += 25
  #     decode.append(alphabet[ascii])
      
  #   else:
  #     decode.append(" ")
  # print ("".join(decode))
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
#hello
check_continue = True
while check_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text,shift,direction)
  choice = input("Do you want to continue? enter yes to continue and no to exit ").lower()
  if choice == 'no':
    check_continue = False
    print("Thanks for using my cipher")
