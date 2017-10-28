
# player use csp helper
def playcsp(listofPos, matrix):
    # do the csp first
    nomine, mine = csp()
    count = 0

    #judge four cases
    # case 1: no nomine and no mine, then do dfs
    if (len(nomine) == 0 & len(mine) == 0):
        count += 1
        return listofPos[count]

    # case 2: no nomine and have mine, then delete mine from dfs path, run dfs
    elif(len(nomine)== 0 & len(mine) != 0):
        for bomb in mine:
            listofPos.remove(bomb)
            matrix[bomb[0]][bomb[1]] = 9
        count += 1
        return listofPos[count]

    # case 3: have nomine and no mine, then click the nomine first
    elif(len(nomine) != 0 & len(mine) == 0):
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        count += 1
        return nomine[0]

    # case 4: have nomine and have mine, then click the nomine first
    else:
        for bomb in mine:
            listofPos.remove(bomb)
            matrix[bomb[0]][bomb[1]] = 9
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        count += 1
        return nomine[0]

# player use logic helper
def playlogic(listofPos, matrix):
    # do the csp first
    nomine, mine = logic()
    count = 0

    #judge four cases
    # case 1: no nomine and no mine, then do dfs
    if (len(nomine) == 0 & len(mine) == 0):
        count += 1
        return listofPos[count]

    # case 2: no nomine and have mine, then delete mine from dfs path, run dfs
    elif(len(nomine)== 0 & len(mine) != 0):
        for bomb in mine:
            listofPos.remove(bomb)
            matrix[bomb[0]][bomb[1]] = 9
        count += 1
        return listofPos[count]

    # case 3: have nomine and no mine, then click the nomine first
    elif(len(nomine) != 0 & len(mine) == 0):
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        count += 1
        return nomine[0]

    # case 4: have nomine and have mine, then click the nomine first
    else:
        for bomb in mine:
            listofPos.remove(bomb)
            matrix[bomb[0]][bomb[1]] = 9
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        count += 1
        return nomine[0]