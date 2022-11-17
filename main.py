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
        for i in range(0, len(line)):
            # If the part of the string is not a zero, add it to the return string
            if (line[i] != "0" and line[i] != "\n"):
                fenString += line[i]
            # If the part of the string is a zero, count all of them until there are not any more
            elif (line[i] == "0"):
                while zeroCounter + i < len(line) and line[i + zeroCounter] == "0":
                    # BUG: Currently prints 87654321 rather than just 8
                    zeroCounter += 1
                    print(zeroCounter)
                fenString += str(zeroCounter)
                i += zeroCounter
                zeroCounter = 0
            else:
                if (counter != 7):
                    fenString += "/"
        counter += 1
    print(fenString)     
                
function()
   
