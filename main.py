# Format:
# Zeros for no pieces
# Letters for other pieces
# Legend:
# k -> King
# q -> Queen
# r -> Rook
# b -> Bishop
# p -> Pawn
# n -> knight
# 0 -> No piece
# CAPITALS: white
# lowercase: black

def function():
    # Ensure the file exists
    try:
        #filename = input("Insert file name:\n")
        fp = open("test.txt", "r+")
    except:
        print("No such file exists")
    # read all lines from file
    linearray = fp.readlines()
    counter = 0
    fenString = ""
    while counter < len(linearray):
        line = linearray[counter]
        zeroCounter = 0
        i = 0
        while i < len(line):
            # If the part of the string is not a zero, add it to the return string
            if (line[i] != "0" and line[i] != "\n"):
                fenString += line[i]
            # If the part of the string is a zero, count all of them until there are not any more
            # BUG: Misses adding the piece right after the end of a run of zeros
            elif (line[i] == "0"):
                while zeroCounter + i < len(line) and line[i + zeroCounter] == "0":
                    zeroCounter += 1
                fenString += str(zeroCounter)
                i += zeroCounter
                if (i >= len(line) - 1):
                    fenString += "/"
                zeroCounter = 0
            else:
                if (counter != 7):
                    fenString += "/"
            i += 1
        counter += 1
    print(fenString)


function()
