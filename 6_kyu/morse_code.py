def decode_morse(morse_code):
    # Remember - you can use the preloaded MORSE_CODE dictionary:
    # For example:

    MORSE_CODE = {}

    MORSE_CODE['. -'] = 'A'
    MORSE_CODE['--...'] = '7'
    MORSE_CODE['...-..-'] = '$'

    return ' '.join(
        [''.join((MORSE_CODE[x] for x in morse_words.split())) for morse_words in morse_code.strip().split('   ')])


# [[MORSE_CODE[x] for x in morse_words.split()]

print(decode_morse("    --... ...-..-   --... ...-..-"))
