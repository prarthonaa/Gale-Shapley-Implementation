# 3600 Stable Matching  Mini Project - Gale Shapley Algorithm code
# Elaine Prarthona Nelson


from random import randint


def returnArrays(lines,k):
    hi = []
    si = []
    # create temp array for hospital preference choices
    h = createTempH(lines,k)
    h = createIntArray(h)
    # # create temp array for school preference choices
    s = createTempS(lines, k)
    s = createIntArray(s)
    # create hi array
    element = ""
    for i in lines[-3]:
        if i == "\n":
            break
        elif i == " ":
            element = int(element)
            hi.append(element)
            element = ""
        else:
            element += i
    # create si array
    element = ""
    for i in lines[-1]:
        if i == "\n":
            break
        elif i == " ":
            element = int(element)
            si.append(element)
            element = ""
        else:
            element += i
    return h, s, hi, si



def createTempH(lines, k):
    temp = []
    i = 3
    while i <= (2+k): # got this from some calculation of the input format
        temp.append(lines[i])
        i += 1
    return temp


def createTempS(lines, k):
    temp = []
    i = 4+k
    while i <= (3+(2*k)): # got this from some calculation from the input format
        temp.append(lines[i])
        i += 1
    return temp


def createIntArray(temp):
    # add elements from temp array to final h array
    a = []
    for line in temp:
        row = []
        rowElement = ""
        for e in line:
            if e == "\n":
                break
            elif e == " ":
                rowElement = int(rowElement)
                row.append(rowElement)
                rowElement = ""
            else:
                rowElement += e
        a.append(row)
    return a


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


if __name__ == "__main__":
    file = open("input.txt", "r")
    lines = file.readlines()
    n = int(lines[0])
    k = int(lines[1])
    # print(lines)
    # print(n, k)

    file.close()

    arrays = returnArrays(lines,k)
    h = arrays[0]
    s = arrays[1]
    hi = arrays[2]
    si = arrays[3]
    # print(h)
    # print(s)
    # print(hi)
    # print(si)

    matches = galeShapley(n,h,hi,s,si)
    with open("output.txt", "w") as file:
        for pair in matches:
            row = ""
            for e in pair:
                e = str(e)
                row += e + " "
            file.write(row)
            file.write("\n")

    file.close()



