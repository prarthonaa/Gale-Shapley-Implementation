#Elaine Prarthona Nelson


from random import randint
import randomInstanceGenerator
import time


def isUnmatched(m, i):
    return m[i] == -1


def hUnmatchedAndNotPropToAll(i, hm, propostioncount, n):
    if hm[i] == -1 and propostioncount[i] != n:
        return True
    else:
        return False


def prefersNewHOverOldH(s, si, newh, student, sm):
    oldh = sm[student]

    rankIndex = si[student]

    prefListOfStudent = s[rankIndex]

    if prefListOfStudent.index(newh) < prefListOfStudent.index(oldh):

        return True
    else:

        return False


def galeShapley(n, h, hi, s, si):
    matches = []
    propositionCount = []
    sm = [-1] * n
    hm = [-1] * n

    for i in range(n):
        propositionCount.append(0)

    hospital = randint(0, n - 1)
    rounds = 0 # track rounds
    while hm[hospital] == -1 and propositionCount[hospital] < n:
        rounds += 1
        rankIndex = hi[hospital]
        prefListOfHospital = h[rankIndex]
        unproposedStudentIndex = propositionCount[hospital]
        student = prefListOfHospital[unproposedStudentIndex]

        if isUnmatched(sm, student):
            pair = [hospital, student]
            matches.append(pair)
            hm[hospital] = student
            sm[student] = hospital
            propositionCount[hospital] += 1


        elif prefersNewHOverOldH(s, si, hospital, student, sm):
            pair = [hospital, student]
            matches.append(pair)
            oldh = sm[student]
            matches.remove([oldh, student])

            hm[oldh] = -1
            hm[hospital] = student
            sm[student] = hospital
            propositionCount[hospital] += 1


        else:
            propositionCount[hospital] += 1

        if -1 in hm:
            while hm[hospital] != -1:
                hospital = randint(0, n - 1)

    return matches, rounds


def test(n, k):
    h = randomInstanceGenerator.preferenceOptions(n, k)

    s = randomInstanceGenerator.preferenceOptions(n, k)

    hi = randomInstanceGenerator.preferenceIndexes(n, k)

    si = randomInstanceGenerator.preferenceIndexes(n, k)

    start = time.time() # track time
    matchArrayandRounds = galeShapley(n, h, hi, s, si)
    end = time.time()
    totalTime = end - start
    rounds = matchArrayandRounds[1]

    print(totalTime)
    return totalTime, rounds


