# Hur börjar jag att skriva ett program?

# Jag funderar igenom strukturen


'''
VISA HUVUDMENY

Upprepa tills spelet är slut
  Spela en omgång av spelet
  Fråga om spelaren vill spela igen
'''


'''
SPELA EN OMGÅNG

Välj ett slumpmässigt ord
Upprepa tills omgången är slut
  Skriv ut ställningen
  Utför gissning
  Kontrollera vinst/förlust
'''

'''
SKRIV UT STÄLLNINGEN

Beräkna delvis dolda ordet
Skriv ut delvis dolda ordet
Skriv ut använda bokstäver
Skriv ut galgen
'''

'''
BERÄKNA DELVIS DOLDA ORDET

Skapa ett tomt nytt ord
Loopa igenom riktiga ordet
  Om bokstaven finns bland gissade bokstäver
    Lägg till bokstaven i det nya ordet
  Annars
    Lägg till ett understreck i det nya ordet
Returnera nya ordet
'''

'''
UTFÖR GISSNING

Fråga vad spelaren gissar på
Upprepa
  Är gissningen ett ord?
    Är det ett ord som spelare inte gissat förut?
      Är ordet korrekt?
        Returnera vinst
      Annars
        Lägg till bland gissade ord
        Öka antalet fel
        Returnera ej vinst
      Annars
        Skriv att spelaren redan gissat bokstaven
  Är gissningen en bokstav?
    Är det en bokstav som spelaren inte gissat förut?
      Ingår bokstaven i ordet?
        Lägg till bland gissade bokstäver
        Är ordet komplett?
          Returnera vinst
        Annars
          Öka antalet fel
          Returnera ej vinst
    Annars
      Skriv att spelaren redan gissat bokstaven
  Annars
    Skriv att inmatningen är felaktig
'''

import random

WORDS = [
    "mikroskop", "citronsyracykeln", "hastighet",
    "derivata", "integral", "kärnkraft", "gravitation",
    "gränsvärde", "jämviktskonstant",
    "buffertsystem", "fällning", "silverklorid",
    "bariumnitrat", "predikatsfyllnad", "attribut",
    "chipspåse", "sextiosju", "halloween", "höstlov",
    "omprov", "komplettering", "titrering"
]

ALLOWED_LETTERS = "abcdefghijklmnopqrstuvwxyzåäö"

def mask_word(correct_word, revealed_letters):
    masked_word = ""
    for letter in correct_word:
        if letter in revealed_letters:
            masked_word += " " + letter.upper() + " "
        else:
            masked_word += " _ "
    return masked_word

def is_revealed(word, revealed_letters):
    for letter in word:
        if letter not in revealed_letters:
            return False
    return True

def is_valid_letter(letter):
    return letter in ALLOWED_LETTERS

def is_valid_word(word):
    for letter in word:
        if not is_valid_letter(letter):
            return False
    return True

def make_guess(correct_word, revealed_letters, guessed_words):
    while True:
        guess = input("Vad gissar du?")
        guess = guess.lower().strip()
        if len(guess)==1:
            if not is_valid_letter(guess):
                print("Otillåten bokstav!")
            elif guess in revealed_letters:
                print("Du har redan gissat den bokstaven!")
            else:
                revealed_letters.append(guess)
                revealed_letters.sort()
                return guess in correct_word, is_revealed(correct_word, revealed_letters)
        elif len(guess)>1:
            if not is_valid_word(guess):
                print("Ordet innehåller otillåtna tecken!")
            elif guess in guessed_words:
                print("Du har redan gissat det ordet!")
            elif guess==correct_word:
                guessed_words.append(guess)
                return True, True
            else:
                return False, False

def print_standing(mistakes, correct_word, revealed_letters):
    masked_word = mask_word(correct_word, revealed_letters)
    print(f"Ordet är: {masked_word}")
    print(f"Du har gissat på bokstäverna: {', '.join(revealed_letters)}")
    print(f"Du har haft {mistakes} fel av max 10")

def play():
    word = random.choice(WORDS)
    guessed_letters = []
    guessed_words = []
    mistakes = 0
    playing = True
    while playing:
        print_standing(mistakes, word, guessed_letters)
        is_correct_guess, is_correct_word = make_guess(word, guessed_letters, guessed_words)
        if not is_correct_guess:
            mistakes += 1       

        if is_correct_word:
            print("Grattis! Du klarade det! Du hade {mistakes} fel!")
            break
        elif mistakes>10:
            print("Attans! Du förlorade! Ordet var {word.upper()}")
            break
        
def main():
    playing = True
    while playing:
        play()
        while True:
            inp = input("Vill du spela igen (J/n)? ")
            inp = inp.lower().strip()
            if inp=="" or inp=="j":
                break
            elif inp=="n":
                playing = False
                break
            
main()