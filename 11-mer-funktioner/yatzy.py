def roll_dice(n):
    '''Roll n dices and return a list with their values'''
    pass

# Gör funktioner för poängräkning
# Ettor, tvåor osv. + par, tretal, fyrtal

def scores_single_value(dice, val):
    '''Ger poäng för slag med en viss siffra (t ex val=1 ger ettor)'''
    pass

def scores_pair(dice):
    '''Returnerar poängen om spelaren väljer par, 0 innebär inget par finns'''

def print_possible_scores(dice):
    print(f"Ettor kan ge {scores_single_value(dice, 1)} poäng")
    print(f"Par kan ge {scores_pair(dice)} poäng")

def main():
    dice = roll_dice(5)
    print_possible_scores(dice)

main()




