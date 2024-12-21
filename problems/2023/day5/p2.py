from shared import get_dataset
from os import getenv

dataset = get_dataset()
p2_test_case_answer: str = "46"


def parse_seed_ranges(input) -> list[tuple[int, int]]:
    seed_ranges = []
    seed_strs = input.split()
    seed_strs.pop(0)

    for i in range(0, len(seed_strs), 2):
        range_start = int(seed_strs[i])
        range_end = range_start + int(seed_strs[i+1])

        seed_ranges.append((range_start, range_end))

    return seed_ranges


def is_valid_seed(seed: int, ranges: list[tuple[int, int]]) -> bool:

    for rng in ranges:
        range_start, range_end = rng

        if range_start <= seed < range_end:
            return True

    return False


def parse_map(input) -> list[tuple[int, int, int]]:
    map = []
    input = input.split()

    for i in range(2, len(input), 3):
        map.append((int(input[i]), int(input[i+1]), int(input[i+2])))

    return map


def is_in_mapline(num_to_check: int, mapline: tuple[int, int, int]) -> bool:
    src_range_start = mapline[1]
    src_range_end = src_range_start + mapline[2]
    return src_range_start <= num_to_check < src_range_end


def is_in_mapline_reverse(num_to_check: int, mapline: tuple[int, int, int]) -> bool:
    des_range_start = mapline[0]
    des_range_end = des_range_start + mapline[2]
    return des_range_start <= num_to_check < des_range_end


def convert_by_line(num_to_convert: int, map_line: tuple[int, int, int]) -> int:
    if map_line == (-1, -1, -1):
        return num_to_convert

    dest_rng_start, src_rng_start, range_length = map_line
    delta = num_to_convert - src_rng_start
    new_num = dest_rng_start + delta

    return new_num


def unvert_by_line(num_to_convert: int, map_line: tuple[int, int, int]) -> int:
    if map_line == (-1, -1, -1):
        return num_to_convert

    dest_rng_start, src_rng_start, range_length = map_line
    delta = num_to_convert - dest_rng_start
    new_num = src_rng_start + delta

    return new_num


def convert_by_map(num_to_convert: int, map: list[tuple[int, int, int]]) -> int:
    key = (-1, -1, -1)

    for mapline in map:
        if is_in_mapline(num_to_convert, mapline):
            key = mapline

    new_num = convert_by_line(num_to_convert, key)

    return new_num


def unvert_by_map(num_to_convert: int, map: list[tuple[int, int, int]]) -> int:
    key = (-1, -1, -1)

    for mapline in map:
        if is_in_mapline_reverse(num_to_convert, mapline):
            key = mapline

    new_num = unvert_by_line(num_to_convert, key)

    return new_num


def get_location_from_seed(seed: int, all_maps: list[list[tuple[int, int, int]]]) -> int:
    converted_value = seed

    for map in all_maps:
        converted_value = convert_by_map(converted_value, map)

    return converted_value


def get_seed_from_location(loc: int, all_maps: list[list[tuple[int, int, int]]]) -> int:
    unverted_value = loc
    reversed_maps = []

    for i in range(len(all_maps) - 1, -1, -1):
        reversed_maps.append(all_maps[i])

#     print(all_maps)
# #     all_maps.reverse()
#     print(reversed_maps)

    for map in reversed_maps:
        unverted_value = unvert_by_map(unverted_value, map)

    return unverted_value


def get_src_starts(map: list[tuple[int, int, int]]) -> list[int]:
    src_starts = []
    for mapline in map:
        src_starts.append(mapline[0])
    return src_starts


def get_des_starts(map: list[tuple[int, int, int]]) -> list[int]:
    des_starts = []
    for mapline in map:
        des_starts.append(mapline[1])
    return des_starts


def get_range_lengths(map: list[tuple[int, int, int]]) -> list[int]:
    range_lengths = []
    for mapline in map:
        range_lengths.append(mapline[2])
    return range_lengths


def print_conversion_table(range_start: int, range_end: int, all_maps: list[list[tuple[int, int, int]]]):
    lines = ["Seeds  | ",
             "Soil   | ",
             "Fert   | ",
             "Water  | ",
             "Light  | ",
             "Temp   | ",
             "Humid  | ",
             "Loc    | "]

    for seed in range(range_start, range_end, 1):

        converted_num = seed

        for i in range(len(all_maps)):
            lines[i] += f" {converted_num} "
            converted_num = convert_by_map(converted_num, all_maps[i])

        lines[len(all_maps)] += f" {converted_num} "

    for line in lines:
        print(line)

    return


def test_conversion(seed: int, all_maps: list[list[tuple[int, int, int]]]):
    loc = get_location_from_seed(seed, all_maps)
    new_seed = get_seed_from_location(loc, all_maps)
    warning = "- FAIL"

    if new_seed == seed:
        warning = ""

    print(
        f"Seed {seed} gives you location {loc} gives you seed {new_seed} {warning}")
    return


def test_unversion(loc: int, all_maps: list[list[tuple[int, int, int]]]):
    seed = get_seed_from_location(loc, all_maps)
    new_loc = get_location_from_seed(seed, all_maps)
    warning = "- FAIL"

    if new_loc == loc:
        warning = ""

    print(
        f"Location {loc} gives you seed {seed} gives you location {new_loc} {warning}")
    return


def p2() -> str:
    # Solve code here, return string to submit
    seed_ranges = parse_seed_ranges(dataset[0])
    maps = []

    dataset.pop(0)

    for map in dataset:
        maps.append(parse_map(map))

    loc = 0
    answer = 0
    answer_found = False

    print(get_seed_from_location(19, maps))

    # for i in range(100):
    #     test_unversion(i, maps)

    # print_conversion_table(0, 100, maps)
    # print("\n\n")
    # print_unversion_table(0, 100, maps)

    # for i in range(100):
    #     print(f"Location {i}: seed {get_seed_from_location(i, maps)}")

    # # print(
    # #     f"Program thinks 99 is a valid seed: {is_valid_seed(99, seed_ranges)}")

    while not answer_found:
        seed = get_seed_from_location(loc, maps)

        if is_valid_seed(seed, seed_ranges):
            print(
                f"Valid seed ({get_seed_from_location(loc, maps)}) found at location {loc}")
            answer = loc
            answer_found = True

        loc += 1

        if loc % 10000 == 0:
            print(loc)

    print(answer)

    return f"{answer}"


# Do not modify this code
# Runs unit test on short dataset
# Prints answer on long dataset without tests
if __name__ == '__main__' and not getenv("USE_FULL"):
    print("\n-------Program Debug Text-------")
    p2_answer = p2()
    print("--------------------------------\n")
    assert p2_answer == p2_test_case_answer, f"\n\nfunction p2 returned {'nothing' if p2_answer=='' else p2_answer}\nshould be {p2_test_case_answer}"
    print(f"function p2 returned {p2_answer}\nAnswer is CORRECT")
elif __name__ == '__main__':
    p2_answer = "\n" + p2()
    print(p2_answer)
