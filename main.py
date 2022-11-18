# Piece Format:
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
# Standard Layout:
# rnbqkbnr
# pppppppp
# 00000000
# 00000000
# 00000000
# 00000000
# PPPPPPPP
# RNBQKBNR

# Next Move Format:
# After pieces: "Black" or "White" indicates next move

# Castling Rights Format:
# After next move descriptor, 'K' 'Q' 'k' 'q' indicates which side has not castled
# e.g. ~ Kkq : King side of white, King and Queen side of black all have castling rights

# Halfmove Clock
# After Castling Rights descriptor, some number up to 50 moves, referring to the
# 50 move draw rule describes the number of moves that have been taken without a capture or after pawn move
# Resets after a capture or a pawn has been moved

# Fullmove Counter
# After Halfmove descriptor, some number incremeneted by 1 referring to the number
# of moves by each player, incremented up after each of Black's move

linearray = []
fenString = ""
def pieceFen():
    # Ensure the file exists
    try:
        #filename = input("Insert file name:\n")
        fp = open("test2.txt", "r+")
    except:
        print("No such file exists")
    # read all lines from file
    linearray = fp.readlines()
    counter = 0
    while counter < 8:
        line = linearray[counter]
        zeroCounter = 0
        i = 0
        while i < len(line):
            # If the part of the string is not a zero, add it to the return string
            if (line[i] != "0" and line[i] != "\n"):
                fenString += line[i]
                i += 1
            # If the part of the string is a zero, count all of them until there are not any more
            # BUG: Misses adding the piece right after the end of a run of zeros
            elif (line[i] == "0"):
                while zeroCounter + i < len(line) and line[i + zeroCounter] == "0":
                    zeroCounter += 1
                fenString += str(zeroCounter)
                i += zeroCounter
                zeroCounter = 0
            else:
                if (counter != 7):
                    fenString += "/"
                i += 1    
        counter += 1
    print(fenString)
def castlingFen():
    if (len(linearray) != 0):
        print()    

pieceFen()
