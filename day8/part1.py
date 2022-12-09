from __future__ import annotations
import os

# coord[0] == row / coord[1] == column
def is_visible(coord: tuple[int, int], trees: list[str], tree_value: int):
    
    if coord[0] == 0 or coord[0] == len(trees)-1: return True
    elif coord[1] == 0 or coord[1] == len(trees[0])-1: return True
    
    top = True
    right = True

    # -- check top --
    for i in range(coord[0]): # if the tree is in row 1, i will start in 0 
        if int(trees[i][coord[1]]) >= tree_value: 
            top = False
            break

    # -- check right --
    for i in range(len(trees[0]) - coord[1] - 1):
        if int(trees[coord[0]][coord[1]+1+i]) >= tree_value: 
            right = False
            break

    return top or right

def main():
    input_path = os.path.join(os.path.dirname(__file__), "test.txt")
    with open(input_path, "r") as file:

        trees = []

        while True:
            line = file.readline()
            if not line:
                break

            line = line.strip("\n")

            trees.append(line)

        print(trees)
        for row, line in enumerate(trees):
            for column, tree in enumerate(line):
                tree = int(tree)
                result = is_visible((row, column), trees, tree)
                print((row, column), result)

        file.close()


if __name__ == "__main__":
    main()
