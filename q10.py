text = input("Enter a sentence: ")
frequency = {}

for character in text:
    if character != " ":
        frequency[character] = frequency.get(character, 0) + 1

print("\nCharacter frequencies:")
for character, count in frequency.items():
    print(character, ":", count)

output
Enter a sentence: my name is dhanush

Character frequencies:
m : 2
y : 1
n : 2
a : 2
e : 1
i : 1
s : 2
d : 1
h : 2
u : 1
