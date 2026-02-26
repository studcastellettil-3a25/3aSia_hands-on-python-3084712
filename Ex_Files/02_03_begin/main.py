NAMES = ["patrizioaura", "charlie", "jeffrey", "marza"]
AGES = [20, 21, 22, 23]

patrizioaura = NAMES[0]
charlie = NAMES[1]

patrizioaura_charlie = NAMES[:2]
jeffrey_marza = NAMES[2:]
REVERSE = NAMES[::-1]
EVERY_OTHER = NAMES[::2]

print(sum(AGES))
print(min(AGES))
print(max(AGES))

print(patrizioaura_charlie)
print(jeffrey_marza)
print(REVERSE)
