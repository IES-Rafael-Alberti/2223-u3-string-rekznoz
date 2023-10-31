def str_reverse(string):
    reversed_str = ""
    i = len(string) - 1
    while i >= 0:
        reversed_str += string[i] + "\n"
        i -= 1
    return reversed_str

if __name__ == '__main__':

    lafrase = "Esto es una frase"

    lafrasealreves = str_reverse(lafrase)

    print(lafrasealreves)