from os import path


def parse_stacks(stacks_raw: list[str]):
    stacks = [[], [], [], [], [], [], [], [], []]
    for line in stacks_raw:
        start_index = 0
        stack_to_fill = 0
        end_line = False
        while True:
            if start_index >= len(line):
                break
            index = 0
            try:
                index = line[start_index:].index("[")
            except:
                for _ in range(9-stack_to_fill):
                    stacks[stack_to_fill].append("-")
                    stack_to_fill += 1
                    end_line = True
            if end_line:
                break
            empty_stacks = index/4
            if not (empty_stacks < 1):
                empty_stacks = int(empty_stacks)
                for _ in range(empty_stacks):
                    stacks[stack_to_fill].append("-")
                    stack_to_fill += 1
            if stack_to_fill > 8: break
            stacks[stack_to_fill].append(line[index+start_index+1])
            stack_to_fill += 1
            start_index = start_index + index + 2

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
