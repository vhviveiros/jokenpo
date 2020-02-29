import random

DRAW = 0
PC = 1
USER = 2

options = ['pedra', 'tesoura', 'papel']
results = ['Empate!\n', 'computador', 'usuário']

def compare(pc_entry:int, user_entry:int):
    if pc_entry is user_entry:
        return DRAW
    if pc_entry is 0 and user_entry is 2:
        return USER
    if pc_entry < user_entry or (pc_entry is 2 and user_entry is 0):
        return PC
    return USER

while True:
    user_input = str.lower(input("\nDigite sua entrada:\n"))
    if user_input in options:
        pc_entry = random.randint(0,2)
        result = compare(pc_entry, options.index(user_input))
        print("PC: " + options[pc_entry])
        print(results[0] if result == 0 else "O " + results[result] + " venceu a rodada!\n")
    else:
        print("Entrada Inválida!")

