RICHTER_VALUES = [1.0, 5.0, 9.1, 9.2, 9.5]
JOULES_PER_TNT_TON = 4.184e9

def calculate_energy(richter):
    return 10 ** ((1.5 * richter) + 4.8)

for value in RICHTER_VALUES:
    energy = calculate_energy(value)
    tnt = energy / JOULES_PER_TNT_TON
    print(f"Richter scale value: {value}")
    print(f"Equivalence in joules: {energy}")
    print(f"Equivalence in tons of TNT: {tnt}")
    print()

user_input = float(input("Please enter a Richter scale value: "))
energy = calculate_energy(user_input)
tnt = energy / JOULES_PER_TNT_TON
print(f"Richter scale value: {user_input}")
print(f"Equivalence in joules: {energy}")
print(f"Equivalence in tons of TNT: {tnt}")
