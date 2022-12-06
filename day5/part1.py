from os import path


def parse_stacks(stacks_raw: list[str]):
    stacks = [[], [], [], [], [], [], [], [], []] # saves the stacks from 0 to 8 (1 - 9 in the instructions)
    for line in stacks_raw:
        start_index = 0  # starting for searching "["
        stack_to_fill = 0 # wich stack it is supposed to fill with content
        end_line = False # if the contents from the line are done
        while True: # loops the process of finds "[" -> fill the gaps -> fill the letter
            index = 0 # declares the index where "[" is found
            try:
                index = line[start_index:].index("[")
            except: # if none "[" is found, it means that there's no more letters in the line
                for _ in range(9-stack_to_fill): # fills the remaining spaces with "-" (blanks)
                    stacks[stack_to_fill].append("-")
                    stack_to_fill += 1
                    end_line = True
            if end_line:
                break
            empty_stacks = index/4 # finds how many stacks are missing from the last spot searched
            if not (empty_stacks < 1): # if there's no missing stack, then the spaces (1) divided by 4 is lesser than one (0.25)
                empty_stacks = int(empty_stacks)
                for _ in range(empty_stacks): # fills the empty spaces
                    stacks[stack_to_fill].append("-")
                    stack_to_fill += 1
            if stack_to_fill > 8: break
            stacks[stack_to_fill].append(line[index+start_index+1]) # fills the letter that was found in the beginning with the "[" 
            stack_to_fill += 1
            start_index = start_index + index + 2 # updates the start index so the next search starts from the "]"

    print(stacks)

    return stacks


file_path = path.join(path.dirname(__file__), "input.txt")

with open(file_path) as file:

    done_reading_satcks = False

    stacks_raw = []

    while True:

        line = file.readline()
        if not line:
            break
        else:
            line = line.strip("\n")

        if line.startswith(" 1"):
            file.readline()
            file.readline()
            parse_stacks(stacks_raw)
            done_reading_satcks = True

        if not done_reading_satcks:
            stacks_raw.append(line)
