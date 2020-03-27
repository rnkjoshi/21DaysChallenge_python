def converter(message):
    messageList = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "☹"
    }
    convertedMessage = ''
    for i in messageList:
        convertedMessage += emojis.get(i, i) + " "
    return convertedMessage


message = input("Enter your message : ")
convertedMessage = converter(message)
print(convertedMessage)
