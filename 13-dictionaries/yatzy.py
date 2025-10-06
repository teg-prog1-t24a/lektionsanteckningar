import random

# Som standard kommer vi att slå fem tärningar med sex sidor
# men om vi skulle vilja så kan vi välja andra alternativ
def roll_dice(n=5, sides=6):
    dice = []
    for _ in range(n):
        val = random.randint(1,sides)
        dice.append(val)
    return dice

# Den här funktionen räknar förekomsten av varje värde på tärningen
def calc_frequencies(dice):
    freqs = []
    # Gå igenom de olika valörerna 1-6 och räkna hur många sådana
    # tärningar som finns bland tärningarna
    for i in range(6):
        freq = dice.count(i+1)
        freqs.append(freq)
    return freqs

# Kolla vilken poäng som tärningar av en specifik valör kan ge
def score_single_value(freqs, val):
    return freqs[val-1] * val

# Kolla vilken poäng som flera tärningar av samma valör kan ge
def score_many_values(freqs, num):
    for val in range(6,0,-1):
        if freqs[val-1]>=num:
            return val*num
    return 0
        
# Kolla vilken poäng som kåk kan ge
def score_full_house(dice, freqs):
    if 2 in freqs and 3 in freqs:
        return sum(dice)
    return 0

# Kolla vilken poäng som två par kan ge
def score_two_pair(freqs):
    # Börja med summan 0
    sum = 0
    for val in range(6,0,-1):
        # Kolla om vi har minst två tärningar av valören
        if freqs[val-1]>=2:
            # Kolla nu om summan är över noll
            # I så fall har vi redan hittat ett par
            if sum>0:
                return sum + 2*val
            # Här har vi hittat det första paret så
            # lägg till poängen i sum
            sum += 2*val
    return 0

# Beräkna möjliga poäng i varje kategori
# och returnera som en lista med tuplar
# t ex [ ("ettor", 0), ("tvåor", 3) ]

def get_scores(dice):
    # Beräkna frekvenserna, kan vara bra att ha
    frequencies = calc_frequencies(dice)

    scores = []
    
    scores.append(("ettor", score_single_value(frequencies, 1)))
    scores.append(("tvåor", score_single_value(frequencies, 2)))
    scores.append(("treor", score_single_value(frequencies, 3)))
    scores.append(("fyror", score_single_value(frequencies, 4)))
    scores.append(("femmor", score_single_value(frequencies, 5)))
    scores.append(("sexor", score_single_value(frequencies, 6)))
    
    scores.append(("par", score_many_values(frequencies, 2)))
    scores.append(("tretal", score_many_values(frequencies, 3)))
    scores.append(("fyrtal", score_many_values(frequencies, 4)))

    scores.append(("två par", score_two_pair(frequencies)))
    scores.append(("kåk", score_full_house(dice, frequencies)))

    return scores   

# Skriv ut ett tärningsslag
def print_dice(dice):
    string_list = [str(i) for i in dice]
    dice_as_string = ", ".join(string_list)    
    print(f"Du slog {dice_as_string}")

# Skriv ut alla möjliga poäng
def print_scores(scores):
    for category, score in scores:
        if score>0:
            print(f"Kategorin {category} kan ge {score} poäng")

# Spela en runda i spelet
def play_round():
    dice = roll_dice()
    print_dice(dice)

    scores = get_scores(dice)
    print_scores(scores)

# Här startar programmet
def main():
    while True:
        play_round()

        inp = input("En omgång till? (skriv 'q' för att sluta)")
        if inp=='q':
            break

# Anropa huvudfunktionen
main()