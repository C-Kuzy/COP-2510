'''
 Author: Connor Kouznetsov
 Description: My program is responsible for for converting strings into pig latin. By removing the first letter,
              adding it to the end of the word itself, then adding 'ay' to the end of the word.
'''

#Begin by defining the function latin_of_my_piggie
def latin_of_my_piggie(document: str) -> str:
    outDocument = ''
    sentences = document.replace('\r', '').split('\n')
    
    for sentence in sentences:
        wordList = sentence.split()
        PigLatinWords = []

        for word in wordList:
            if len(word) == 1:
                PigLatinWords.append(word + 'ay')
            else:
                PigLatinWords.append(word[1:] + str(word[0]).lower() + 'ay')

        outDocument += ' '.join(PigLatinWords) + '\n'
    return outDocument

def mainfunct():
    incoming_file = input('Enter the name of the text file: ')
    outgoing_file = "post_" + incoming_file

    try:
        with open(incoming_file, "r") as file:
            content = file.read()

        pig_latin_translation_file = latin_of_my_piggie(content)

        with open(outgoing_file, "w") as file:
            file.write(pig_latin_translation_file)

        print(f'Pig latin translation is in {outgoing_file}')

    except FileNotFoundError:
        print(f"Error, the file {incoming_file} was unable to be located.")
    except Exception as z:
        print(f"We found an error occured at: {z}")

if __name__ == '__main__':
    mainfunct()