from collections import Counter


def parse_line(line):
    return line.strip().replace("-", " ").replace(":", "").split(" ")


def part1(rows):
    
    count = 0
    
    for line in rows:
        rule_min, rule_max, letter, password = parse_line(line)
        
        letter_counter = Counter(password)

        # Check if the string is within the specification according to the policy
        if int(rule_min) <= letter_counter[letter] <= int(rule_max):
            count = count + 1

    return count


def part2(rows):
    count = 0
    for line in rows:
        position1, position2, letter, password = parse_line(line)
        
        length = len(password)
        
        # offset the index by one since the authentication system is array starts at one
        index_a = int(position1) - 1
        index_b = int(position2) - 1

        is_first = index_a < length and password[index_a] == letter
        is_second = index_b < length and password[index_b] == letter

        # xor the results so that only one is valid
        if is_first ^ is_second:
            count = count + 1
    return count


if __name__ == "__main__":
    # Open the file and readlines
    with open('input') as file:
        rows = file.readlines()

        print("The first answer is: {}".format(part1(rows)))
        print("The second answer is: {}".format(part2(rows)))
