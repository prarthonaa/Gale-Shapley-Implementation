# Elaine Prarthona Nelson


from random import randint
import sys


# Random instance generator code, generates random preference lists:


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


def printPreferenceOptions(preferenceListMatrix,k,n):
    
    for i in range(k):
        row = preferenceListMatrix[i]
        print("Preference list ", i, ":", end = " ")
        for j in range(n):
            print(row[j], end=" ")
        print()
        count+=1



def printPreferenceIndexes(indexes,n):
    print("Indexes for each: ", end = " ")
    for i in range(n):
        print(indexes[i], end=" ")
    print()



# Code for the Gale Shapley algorithm:


def isUnmatched(m, i):  # m can be hospital match status array or student
    return m[i] == -1


def hUnmatchedAndNotPropToAll(i, hm, propostioncount, n):
    if hm[i] == -1 and propostioncount[i] != n:
        return True
    else:
        return False


def prefersNewHOverOldH(s, si, newh, student, sm):
    # find which hospital student is matched to currently
    oldh = sm[student]

    # find out which is the students preference list
    rankIndex = si[student]
    # extract the preference list
    prefListOfStudent = s[rankIndex]

    if prefListOfStudent.index(newh) < prefListOfStudent.index(oldh):
        # if index of new hospital lower than index of old hospital then match with new hospital
        # print("Student ", student, "prefers hospital ", newh, " over hospital ", oldh)
        return True
    else:
        # student happy with current match
        # print("Student ", student, "does not prefer hospital ", newh, " over hospital ", oldh)
        return False


def galeShapley(n, h, hi, s, si):
    matches = []
    propositionCount = []  # keeps track of proposition
    # Array to track whether or not they elements are matched
    sm = [-1] * n
    hm = [-1] * n

    for i in range(n):
        propositionCount.append(0)

    hospital = randint(0, n - 1)  # pick first random hospital

    while hm[hospital] == -1 and propositionCount[hospital] < n:

        rankIndex = hi[hospital]  # find which ranking hospital prefers
        prefListOfHospital = h[rankIndex]  # get the preference list
        unproposedStudentIndex = propositionCount[hospital]  # find which student index is next to propose to
        student = prefListOfHospital[unproposedStudentIndex]  # get student number from the preference list

        if isUnmatched(sm, student):  # if student is unmatched add h-s to matches
            pair = [hospital, student]
            matches.append(pair)
            hm[hospital] = student  # update the arrays that track matches
            sm[student] = hospital
            propositionCount[hospital] += 1  # update number of propositions


        elif prefersNewHOverOldH(s, si, hospital, student,
                                 sm):  # if h preferred to previous match of s, replace new h with old h
            pair = [hospital, student]
            matches.append(pair)
            oldh = sm[student]
            matches.remove([oldh, student])  # remove the old pair from matches array

            # replace old match with new match

            hm[oldh] = -1  # update the arrays that track matches
            hm[hospital] = student
            sm[student] = hospital
            propositionCount[hospital] += 1  # update number of propositions


        else:  # student rejects
            propositionCount[hospital] += 1

        # pick another unmatched hos if there are unmatched hospitals left
        if -1 in hm:
            while hm[hospital] != -1:
                hospital = randint(0, n - 1)

    return matches


def printMatches(matches):
    for i in matches:
        print("Hospital ", i[0], "matches with student", i[1])


if __name__ == "__main__":

    if 3 >= len(sys.argv) >= 2:
        n = int(sys.argv[1])
        if len(sys.argv) == 2:  # if value of k not provided then k=n
            k = int(sys.argv[1])
        else:
            k = int(sys.argv[2])

            h = preferenceOptions(n, k)
            s = preferenceOptions(n, k)
            si = preferenceIndexes(n, k)
            hi = preferenceIndexes(n, k)

            print("Possible ranking/preference lists a hospital chooses from:")
            printPreferenceOptions(h,k,n)
            print()
            print("Possible ranking/preference lists set a student chooses from:")
            printPreferenceOptions(s,k,n)
            print()
            print("Indexes of chosen preference lists for hospitals:")
            printPreferenceIndexes(hi,n)
            print()
            print("Indexes of chosen preference lists for students:")
            printPreferenceIndexes(si,n)
            print()

            # perform gale-shapley:
            matches = galeShapley(n, h, hi, s, si)

            print("Stable matches that have been created:")
            printMatches(matches)
            print("Algorithm complete!")



    else:
        print('Error in inputs. Try again.')
