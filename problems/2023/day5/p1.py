from shared import get_dataset
from os import getenv

dataset = get_dataset()
p1_test_case_answer: str = "ENTER TEST ANSWER HERE"


def parse_seeds(input) -> list[int]:
    seeds = []
    seed_list = input.split()
    seed_list.pop(0)

    for seed in seed_list:
        seeds.append(int(seed))

    return seeds


def parse_map(input) -> list[tuple[int, int, int]]:
    map = []
    input = input.split()

    for i in range(2, len(input), 3):
        map.append((int(input[i]), int(input[i+1]), int(input[i+2])))

    return map


def is_in_mapline(num_to_check: int, mapline: tuple[int, int, int]) -> bool:
    src_range_start = mapline[1]
    src_range_end = src_range_start + mapline[2]
    if src_range_start <= num_to_check < src_range_end:
        return True
    else:
        return False


def convert_by_line(num_to_convert: int, map_line: tuple[int, int, int]) -> int:
    dest_rng_start, src_rng_start, range_length = map_line
    delta = num_to_convert - src_rng_start
    new_num = dest_rng_start + delta

    return new_num


def convert_by_map(num_to_convert: int, map: list[tuple[int, int, int]]) -> int:
    key = (0, 0, 0)

    for mapline in map:
        if is_in_mapline(num_to_convert, mapline):
            key = mapline

    new_num = convert_by_line(num_to_convert, key)

    return new_num


def get_seed_location(seed: int, all_maps: list[list[tuple[int, int, int]]]) -> int:
    converted_value = seed

    for map in all_maps:
        converted_value = convert_by_map(converted_value, map)

    return converted_value


def p1() -> str:
    # Solve code here, return string to submit
    seeds = parse_seeds(dataset[0])
    maps = []

    dataset.pop(0)

    for map in dataset:
        maps.append(parse_map(map))

    answer = float("inf")

    for seed in seeds:
        seed_location = get_seed_location(seed, maps)
        if seed_location < answer:
            answer = seed_location

    print(answer)

    # print(f"seeds: {seeds}")
    # print(f"maps: {maps}")

    return f"{answer}"


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
