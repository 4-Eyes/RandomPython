searchTable = [ ["E","R","O","G","A"],
                ["O","G","G","G","E"],
                ["E","A","G","E","W"],
                ["P","E","G","G","E"],
                ["I","N","E","G","A"] ]

def checkDiagonals(grid, gridSize, word, pos):
    matches = []
    wordSize = len(word)
    # check \ diagonal
    rightBotTopLeft = (pos[0] - (wordSize - 1) >= 0 and pos[1] - (wordSize - 1) >= 0, [])
    topLeftRightBot = (pos[0] + (wordSize - 1) < gridSize[0] and pos[1] + (wordSize - 1) < gridSize[1], [])
            
    # check / diagonal
    leftBotTopRight = (pos[0] - (wordSize - 1) >= 0 and pos[1] + (wordSize - 1) < gridSize[1], [])
    topRightLeftBot = (pos[0] + (wordSize - 1) < gridSize[0] and pos[1] - (wordSize - 1) >= 0, [])

    for i in range(wordSize):
        if rightBotTopLeft[0]:
            if grid[pos[0] - i][pos[1] - i] == word[i]:
                rightBotTopLeft[1].append((pos[0] - i, pos[1] - i))
                if i == wordSize - 1:
                    matches.append(rightBotTopLeft[1])
            else:
                rightBotTopLeft = (False, rightBotTopLeft[1])
        if topLeftRightBot[0]:
            if grid[pos[0] + i][pos[1] + i] == word[i]:
                topLeftRightBot[1].append((pos[0] + i, pos[1] + i))
                if i == wordSize - 1:
                    matches.append(topLeftRightBot[1])
            else:
                topLeftRightBot = (False, topLeftRightBot[1])
        if leftBotTopRight[0]:
            if grid[pos[0] - i][pos[1] + i] == word[i]:
                leftBotTopRight[1].append((pos[0] - i, pos[1] + i))
                if i == wordSize - 1:
                    matches.append(leftBotTopRight[1])
            else:
                leftBotTopRight = (False, leftBotTopRight[1])
        if topRightLeftBot[0]:
            if grid[pos[0] + i][pos[1] - i] == word[i]:
                topRightLeftBot[1].append((pos[0] + i, pos[1] - i))
                if i == wordSize - 1:
                    matches.append(topRightLeftBot[1])
            else:
                topRightLeftBot = (False, topRightLeftBot[1])
    return matches

def checkHorizontalVertical(grid, gridSize, word, pos):
    matches = []
    wordSize = len(word)
    leftToRight = (pos[1] + (wordSize - 1) < gridSize[1], [])
    rightToLeft = (pos[1] - (wordSize - 1) >= 0, [])
    upToDown = (pos[0] + (wordSize - 1) < gridSize[0], [])
    downToUp = (pos[0] - (wordSize -1) >= 0, [])
    for i in range(wordSize):
        if leftToRight[0]:
            if grid[pos[0]][pos[1] + i] == word[i]:
                leftToRight[1].append((pos[0], pos[1] + i))
                if i == wordSize - 1:
                    matches.append(leftToRight[1])
            else:
                leftToRight = (False, leftToRight[1])
        if rightToLeft[0]:
            if grid[pos[0]][pos[1] - i] == word[i]:
                rightToLeft[1].append((pos[0], pos[1] - i))
                if i == wordSize - 1:
                    matches.append(rightToLeft[1])
            else:
                rightToLeft = (False, rightToLeft[1])
        if upToDown[0]:
            if grid[pos[0] + i][pos[1]] == word[i]:
                upToDown[1].append((pos[0] + i, pos[1]))
                if i == wordSize - 1:
                    matches.append(upToDown[1])
            else:
                upToDown = (False, upToDown[1])
        if downToUp[0]:
            if grid[pos[0] - i][pos[1]] == word[i]:
                downToUp[1].append((pos[0] - i, pos[1]))
                if i == wordSize - 1:
                    matches.append(downToUp[1])
            else:
                downToUp = (False, downToUp[1])
    return matches

def findWord(grid, word):
    ySize = len(grid)
    xSize = None
    for i in range(ySize):
        if xSize == None:
            xSize = len(grid[i])
        for j in range(xSize):
            diagMatch = checkDiagonals(grid, (ySize, xSize), word, (i, j))
            vertHorMatch = checkHorizontalVertical(grid, (ySize, xSize), word, (i, j))
            if len(diagMatch) > 0 or len(vertHorMatch) > 0:
                for coords in diagMatch + vertHorMatch:
                    yield coords


for match in findWord(searchTable, "PEGGE"):
    print(match)