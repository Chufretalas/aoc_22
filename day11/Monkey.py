from dataclasses import dataclass

@dataclass()
class Monkey():
    items: list[int]
    operation_str: str
    test_number: int
    true_monkey: int
    false_monkey: int

    def __str__(self) -> str:
        return f"(items: {len(self.items)} | operation: {self.operation_str} | test: {self.test_number} | true: {self.true_monkey} | false: {self.false_monkey})"