import CSP
import logic
# player use csp helper
def playcsp(listofPos, matrix, count):
    # print count
    # do the csp first
    mine, nomine = CSP.csp(matrix)
    # print mine
    # print nomine
    # print listofPos
    # print "-----------------------"
    #judge four cases
    # case 1: no nomine and no mine, then do dfs
    if (len(nomine) == 0 and len(mine) == 0):
        return listofPos[count],listofPos,matrix

    # case 2: no nomine and have mine, then delete mine from dfs path, run dfs
    elif(len(nomine)== 0 and len(mine) != 0):
        for bomb in mine:
            if bomb in listofPos:
                listofPos.remove(bomb)
                matrix[bomb[0]][bomb[1]] = 9

        # for cell in matrix:
        #     print cell
        # print listofPos
        return listofPos[count],listofPos,matrix

    # case 3: have nomine and no mine, then click the nomine first
    elif(len(nomine) != 0 and len(mine) == 0):
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        return nomine[0], listofPos,matrix

    # case 4: have nomine and have mine, then click the nomine first
    else:
        for bomb in mine:
            if bomb in listofPos:
                listofPos.remove(bomb)
                matrix[bomb[0]][bomb[1]] = 9
        # print listofPos
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        return nomine[0], listofPos,matrix

# player use logic helper
def playlogic(listofPos, matrix, count):
    # print count
    # do the csp first
    mine, nomine = logic.solver(listofPos, matrix, count)
    # print mine
    # print nomine
    # print listofPos
    # print "-----------------------"
    #judge four cases
    # case 1: no nomine and no mine, then do dfs
    if (len(nomine) == 0 and len(mine) == 0):
        return listofPos[count],listofPos,matrix

    # case 2: no nomine and have mine, then delete mine from dfs path, run dfs
    elif(len(nomine)== 0 and len(mine) != 0):
        for bomb in mine:
            if bomb in listofPos:
                listofPos.remove(bomb)
                matrix[bomb[0]][bomb[1]] = 9

        # for cell in matrix:
        #     print cell
        # print listofPos
        return listofPos[count],listofPos,matrix

    # case 3: have nomine and no mine, then click the nomine first
    elif(len(nomine) != 0 and len(mine) == 0):
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        return nomine[0], listofPos,matrix

    # case 4: have nomine and have mine, then click the nomine first
    else:
        for bomb in mine:
            if bomb in listofPos:
                listofPos.remove(bomb)
                matrix[bomb[0]][bomb[1]] = 9
        # print listofPos
        counting = count
        for safe in nomine:
            listofPos.insert(counting, safe)
            counting += 1
        return nomine[0], listofPos,matrix

