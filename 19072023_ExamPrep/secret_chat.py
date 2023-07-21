def decrypting_message(message):

    while True:
        command = input()

        if command == "Reveal":
            return f"You have a new text message: {message}"

        command = command.split(":|:")
        action = command[0]

        if action == "InsertSpace":
            index = command[1]
            message = message[:int(index)] + " " + message[int(index):]
            print(message)

        elif action == "Reverse":
            substring = command[1]
            if substring in message:
                message = message.replace(substring, "", 1)
                message = message + substring[::-1]
                print(message)
            else:
                print("error")

        elif action == "ChangeAll":
            substring = command[1]
            replacement = command[2]
            message = message.replace(substring, replacement)
            print(message)


input_message = input()
print(decrypting_message(input_message))
