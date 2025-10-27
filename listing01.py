greetings = "Hi Hello Greetings".split()

user_statement = input("Your Statement: ")
user_token_sequence = user_statement.split()

if user_token_sequence[0] in greetings:
    bot_reply = "Thermonuclear War is a strange game. "
    bot_reply += "The only winning move is NOT TO PLAY."
else:
    bot_reply = "Would you like to play a nice game of chess?"

print(bot_reply)
