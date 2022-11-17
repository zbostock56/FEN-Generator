# Format:
# Zeros for no pieces
# Letters for other pieces
# Legend (not case sensitive):
# k -> King
# q -> Queen
# r -> Rook
# b -> Bishop
# p -> Pawn
# 0 -> No piece

def main():
    try:
        filename = input("Insert file name:\n")
    except:
        print("No such file exists")
    # Open for read and write
    file = open(filename, "r+")
