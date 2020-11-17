def findMountain(heightsMap):
    a = 0
    row_max = 0
    column_max = 0
    for row in range(len(heightsMap)):
        for column in range(len(heightsMap)):
            if len(heightsMap)==1:
                return 0, heightsMap.index(max(heightsMap))
            if heightsMap[row][column] > a:
                a = heightsMap[row][column]
                row_max = row
                column_max = column
    return row_max, column_max
