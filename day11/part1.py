import os
from Monkey import Monkey


def main():
    input_path = os.path.join(os.path.dirname(__file__), "example.txt")
    with open(input_path, "r") as file:

        lines = []

        while True:
            line = file.readline()
            if not line:
                break

            line = line.strip()

            if line != "":
                lines.append(line)

            if len(lines) == 6:
                # ---- items ----
                items = []
                items_str = lines[1]
                items_str = items_str[15:].strip().replace(",", "")
                for item in items_str.split():
                    items.append(int(item))

                # ---- operation_str ----
                operation_str: str = lines[2]
                index = operation_str.index("old") + 4
                operation_str = operation_str[index:]

                # ---- test_number ----
                test_number_str: str = lines[3]
                index = test_number_str.index("by") + 3
                test_number_str = test_number_str[index:]
                test_number = int(test_number_str)

                # ---- true_monkey ----
                true_monkey_str: str = lines[4]
                index = true_monkey_str.index("monkey") + 7
                true_monkey_str = true_monkey_str[index:]
                true_monkey = int(true_monkey_str)

                # ---- false_monkey ----
                false_monkey_str: str = lines[5]
                index = false_monkey_str.index("monkey") + 7
                false_monkey_str = false_monkey_str[index:]
                false_monkey = int(false_monkey_str)

                new_monkey = Monkey(items, operation_str, test_number,
                                    true_monkey, false_monkey)

                print(new_monkey)

                lines = []

        file.close()


if __name__ == "__main__":
    main()
