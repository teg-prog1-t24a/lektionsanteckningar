# Med loopar och teckengrafik kan vi
# skapa enkla (och svårare) mönster

# Här skapar ´vi en triangel
# *
# **
# ***
# ****
# *****

storlek = 5
for rad in range(storlek):
    for stjärna in range(rad+1):
        # Med end="" på slutet så stannar print på samma rad
        print("*", end="")
     # Mellan varje rad gör vi en ny rad med en tom print
    print()
