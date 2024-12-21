from shared import get_dataset


def apply_rule(rule: tuple[str, str, str], number_of_times):
    left, right, middle = rule
    starting_pair = left + right
    new_left = left + middle
    new_right = middle + right

    pair_count[starting_pair] -= 1 * number_of_times
    pair_count[new_left] += 1 * number_of_times
    pair_count[new_right] += 1 * number_of_times

    letter_count[middle] += 1 * number_of_times

    return


dataset = get_dataset()


template = dataset[0]
rules = dataset[1:]

letter_count = {}
pair_count = {}
rule_book = {}


for rule in rules:
    left, right, middle = rule[0], rule[1], rule[6]
    rule_book[left + right] = (left, right, middle)
    pair_count[left + right] = 0
    letter_count[left] = 0
    letter_count[right] = 0
    letter_count[middle] = 0

for i in range(len(template) - 1):
    letter_count[template[i]] += 1

    pair = template[i] + template[i+1]
    pair_count[pair] += 1

letter_count[template[len(template) - 1]] += 1


for i in range(40):
    print(i)
    current_pair_count = {k: v for k, v in pair_count.items()}

    for pair in current_pair_count:
        rule = rule_book[pair]
        apply_rule(rule, current_pair_count[pair])

max_letter_count = 0
min_letter_count = 9999999999999999

for letter in letter_count:
    if letter_count[letter] > max_letter_count:
        max_letter_count = letter_count[letter]
    elif letter_count[letter] < min_letter_count:
        min_letter_count = letter_count[letter]

# print(max(letter_count.values()) - min(letter_count.values()))
print(max_letter_count - min_letter_count)
