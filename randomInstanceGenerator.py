# Stable Matching  Mini Project Random instance generator code
# Elaine Prarthona Nelson


from random import randint
import sys


def preferenceOptions(n, k):
    preferenceListMatrix = []
    while len(preferenceListMatrix) != k:
        kline = []
        while len(kline) != n:
            rank = randint(0, n - 1)
            if rank not in kline:
                kline.append(rank)
        preferenceListMatrix.append(kline)

    return preferenceListMatrix


def preferenceIndexes(n, k):
    indexes = []
    while len(indexes) != n:
        choice = randint(0, k - 1)
        indexes.append(choice)
    return indexes


def printPreferenceOptions(preferenceListMatrix):
    s = ""
    for row in preferenceListMatrix:
        r = ""
        for i in row:
            i = str(i)
            r += i + " "
        s += r + "\n"
    return s


def printPreferenceIndexes(indexes):
    s = ""
    for i in indexes:
        i = str(i)
        s += i + " "
    return s



if __name__ == "__main__":

    n = (sys.argv[1])
    if 3 >= len(sys.argv) >= 2:
        if len(sys.argv) == 2:  # if value of k not provided then k=n
            k = (sys.argv[1])
        else:
            k = (sys.argv[2])

        with open("input.txt", "w") as file:
            file.write(n + "\n")
            file.write(k + "\n")
            n = int(n)
            k = int(k)
            file.write("\n")
            h = preferenceOptions(n,k)
            s = preferenceOptions(n,k)
            hi = preferenceIndexes(n,k)
            si = preferenceIndexes(n,k)
            # print(printPreferenceOptions(h))
            # print(printPreferenceOptions(s))
            # print(printPreferenceIndexes(hi))
            # print(printPreferenceIndexes(si))
            file.write(printPreferenceOptions(h))
            file.write("\n")
            file.write(printPreferenceOptions(s))
            file.write("\n")
            file.write(printPreferenceIndexes(hi))
            file.write("\n")
            file.write("\n")
            file.write(printPreferenceIndexes(si))

            file.close()

    else:
        print('Error in inputs. Try again.')
