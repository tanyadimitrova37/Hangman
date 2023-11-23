head = ""
body_upper = ""
left_arm = ""
right_arm = ""
body_lower = ""
left_leg = ""
right_leg = ""
list_of_letters = []
list_of_said_letters = []

print("Enter keyword: ", end=" ")
keyword = str(input())

def hanger():
    print(f"  ______\n", f" |    |\n", f" |    {head}\n",
          f" |   {left_arm}{body_upper}{right_arm} \n", f" |    {body_lower}\n",
          f" |   {left_leg} {right_leg} \n", "_|_")

def list_letters():
    for symbol in range(0, len(keyword)):
        list_of_letters.append(keyword[symbol])
    return list_of_letters

def insert_letter():
    print("Enter a letter ", end=" ")
    curr_letter = str(input())
    if curr_letter in list_of_said_letters:
        print("You already tried that letter! Try another one - ", end="")
        return insert_letter()
    else:
        list_of_said_letters.append(curr_letter)
    return curr_letter

def play():
    hanger()
    fields = "_" * len(keyword)
    print("Empty fields: ", fields)
    check_list = list_letters()
    mistakes_counter = 0
    while True:
        player_letter = insert_letter()

        if player_letter in keyword:
            indices = [i for i, letter in enumerate(keyword) if letter == player_letter]
            for index in indices:
                fields = fields[:index] + player_letter + fields[index + 1:]
            print(fields)

        if player_letter in check_list:
            check_list.remove(player_letter)
            if player_letter in check_list:
                check_list.remove(player_letter)

            if len(check_list) == 0:
                print(f"You guessed the word! - {keyword}")
                break

        else:
            mistakes_counter += 1
            if mistakes_counter == 1:
                global head
                head = 'O'
                print("Try again")
            elif mistakes_counter == 2:
                global body_upper
                body_upper = '|'
                print("Try again")
            elif mistakes_counter == 3:
                global left_arm
                left_arm = "/"
                print("Try again")
            elif mistakes_counter == 4:
                global right_arm
                right_arm = "\\"
                print("Try again")
            elif mistakes_counter == 5:
                global body_lower
                body_lower = "|"
                print("Try again")
            elif mistakes_counter == 6:
                global left_leg
                left_leg = "/"
                print("Try again")
            elif mistakes_counter == 7:
                global right_leg
                right_leg = "\\"
                print("You got hanged!")
                print(f"The word was '{keyword}'.")
                break
        print(f"Letters said: {list_of_said_letters}")
        print(hanger())

play()
