import os

def parse_list(list_str: str) -> tuple[list, int]:
    new_list = []
    index = 0
    while index < len(list_str):
        char = list_str[index]
        
        if char == "[":
            sub_list, jump = parse_list(list_str[index+1:])
            new_list.append(sub_list)
            index += jump

        if char.isnumeric():
            number = []
            number.append(list_str[index])
            i = index + 1
            while True:
                if list_str[i].isnumeric():
                    number.append(list_str[i])
                else:
                    break
                index += 1
                i += 1
            new_list.append(int("".join(number)))

        if char == "]":
            break

        index += 1

    return new_list, index + 1
            

def main():
    input_path = os.path.join(os.path.dirname(__file__), "example.txt")
    with open(input_path, "r") as file:

        pairs: list[list] = []

        while True:
            line = file.readline()
            if not line:
                break

            line = line.strip()

            if line == "": continue

            packet, _ = parse_list(line[1:])

            print(packet)

        # more logic here

        file.close()


if __name__ == "__main__":
    main()
