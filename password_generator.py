import secrets
from math import floor
import itertools

special_characters = [
  "!", "\"", "#", "$", "%", "&", "\'", "()", "*", "+", "-", ".", "/", ":", ";",
  "<", "=", ">", "?", "@", "[", "]", "^", "_", "`", "{", "|", "}", "~"
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
letters = [
  "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
  "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]
letters_upper = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def ask_user():
    if input("\nDo you want to create a password? (y/n) ") == "y":
        generate_password()


def generate_password():
  number_characters = int(input("\nEnter reqired length of password which must be greater than 4 and less than 21: "))
  if number_characters > 20:
    print("\nPassword must be 20 characters or less")
  elif number_characters < 5:
    print("\nPassword must be more than 4 characters")

  else:
    #check if password length is divisible by four
    if (number_characters % 4 == 0):
      selection = int(number_characters / 4)

      #Generate list for each selection
      special_char_selection = secrets.SystemRandom().choices(special_characters, k=selection)

      numbers_selection = secrets.SystemRandom().choices(numbers, k=selection)

      letters_selection = secrets.SystemRandom().choices(letters, k=selection)

      letters_upper_selection = secrets.SystemRandom().choices(letters_upper, k=selection
      )


      #Generate final selection
      final_selection = special_char_selection + numbers_selection + letters_selection + letters_upper_selection

      secrets.SystemRandom().shuffle(final_selection)

      print("Your ", number_characters, " character password is: ", *final_selection, sep="")

    else:
      mod_list = []
      mod_list_final = []
      combined_characters = []

      #Define number of characters from each list when required password lengtth is divided by 4
      selection = number_characters // 4
      

      #Define number of characters remaining
      remainder_selection = (number_characters - selection * 4)
      

      #Generate list for each character using selection. Loop 'slection' numberof times over each list randomly selecting 1 character each time

      for a in range(0, selection):
        for seq in (special_characters,numbers,letters,letters_upper,)[:1]:
          for i in range(0, 1):
            mod_spec_char = secrets.SystemRandom().choices(special_characters, k=1)
            mod_num =  secrets.SystemRandom().choices(numbers, k=1)
            mod_letters_lower = secrets.SystemRandom().choices(letters, k=1)
            mod_letters_upper = secrets.SystemRandom().choices(letters_upper, k=1)

            mod_list = mod_spec_char + mod_num + mod_letters_lower + mod_letters_upper
            

            mod_list_final.append(mod_list)

      #Generate list for remaining characters
      remainder_chars = special_characters + numbers + letters + letters_upper

      remainder_chars_choice = secrets.SystemRandom().choices(remainder_chars, k=remainder_selection)

      #Generate final list
      combined_characters = remainder_chars_choice + mod_list_final
      final_selection = list(itertools.chain().from_iterable(combined_characters))

      #Shuffle final selection and print
      secrets.SystemRandom().shuffle(final_selection)
      print("Your ", number_characters, " password is: ", *final_selection, sep="")

ask_user()