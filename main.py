from math import sqrt

#### Fonction secondaire


def isprime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
        else:
            return True

    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
