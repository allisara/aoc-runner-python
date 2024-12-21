from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "21"

class Block():
    def __init__(self, length: int) -> None:
        self.length = length
        self.earliest_possible = 0
        self.latest_possible = 0
        self.in_block = False
        self.completed = False
    


def p1() -> str:
    # Solve code here, return string to submit
    print(get_possible_values(dataset[0]))

    return ""


def create_blocks(record:tuple[str, list[int]]) -> list[]:
    blocks = []
    
    max_length = len(record[0])
    
    for length in record[1]:
        blocks.append(Block(length))
        
    earliest = 0
    
    for block in blocks:
        block.earliest_possible = earliest
        earliest += block.length +1
        
    blocks.reverse()
    
    latest = max_length - 1
    
    for block in blocks:
        block.latest_possible = latest
        latest -= (block.length + 1)   
    
    
    return blocks


def get_possible_values(record: tuple[str, list[int]]) -> list[list[str]]:

    possible_conditions = []

    for space in record[0]:
        possible_values = []
        if space == "?":
            possible_values = ["#", "."]
        else:
            possible_values = [space]
        possible_conditions.append(possible_values)

    return possible_conditions


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p1_answer = p1()
    print("--------------------------------\n")
    assert p1_answer == p1_test_case_answer, f"\n\nfunction p1 returned {'nothing' if p1_answer=='' else p1_answer}\nshould be {p1_test_case_answer}"
    print(f"function p1 returned {p1_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p1_answer = "\n" + p1()
    print(p1_answer)
