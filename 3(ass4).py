def ispangram(s) :
    alpha = set("abcdefghijklmnopqrstuvwxyz")
    return set(s.lower())>= alpha
s=input("Enter a sentence: ")
if ispangram(s) :
    print("Pangram")
else :
    print("Not Pangram")
# we promtly judged antique ivory buckles for the next prize