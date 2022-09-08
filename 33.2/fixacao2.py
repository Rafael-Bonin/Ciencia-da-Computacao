nums = input("insira numero naturais aqui, separados por espaco: ")

nums_arr = nums.split(" ")

sum = 0

for n in nums_arr:
    if not n.isdigit():
        print(f"Erro ao somar valores, {n} nao e um digito.")
    else:
        sum += int(n)

print(f"a soma dos valores validos e: {sum}")
