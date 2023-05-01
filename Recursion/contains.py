def contains_inappropriate_language(message):
    inappropriate_words = ["puta", "perra", "culero"]  # add more as needed
    for word in message.split():
        if word.lower() in inappropriate_words:
            return True
    return False

print(contains_inappropriate_language('ERES una PERRA'))
