import random

número_aleatório = random.randint(0, 5)

tent = int(input("tente adivinhar o número escolhido pelo computador entre 0 e 5"))
if tent == número_aleatório:
    print(f"parabens!!! você acertou o número era {número_aleatório} que sorte!")
else:
    print(f"putz você errou o número era {número_aleatório} mais sorte na proxima :C")
    