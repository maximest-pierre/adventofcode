import re

with open('input') as file:
    content = file.read().split("\n\n")
    passports = [re.split("[\n\s]", line) for line in content]
    pass_dict = [
        dict([(line.split(":")) for line in passport]) for passport in passports
    ]

def part1(pass_dict):
    result = []
    for passport in pass_dict:
        if len(passport) >= 8:
            result.append(passport)
        elif len(passport) == 7 and 'cid' not in passport.keys():
            result.append(passport)
    return result

def part2(pass_dict):
    result = []
    pass_dict = part1(pass_dict)
    byr = range(1920, 2003)
    iyr = range(2010, 2021)
    eyr = range(2020, 2031)
    hgt = [f"{num}cm" for num in range(150, 194)] + [
        f"{num}in" for num in range(59, 77)
    ]
    hcl = int("ffffff", 16)
    ecl = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for passport in pass_dict:
        if (
            int(passport["byr"]) in byr
            and int(passport["iyr"]) in iyr
            and int(passport["eyr"]) in eyr
            and passport["hgt"] in hgt
            and passport["hcl"][0] == "#"
            and len(passport["hcl"]) == 7
            and int(passport["hcl"].strip("#"), 16) <= hcl
            and passport["ecl"] in ecl
            and len(passport["pid"]) == 9
        ):
            result.append(passport)
    return result


if __name__ == '__main__':
    print("The first answer is: {}".format(part1(pass_dict)))
    print("The second answer is: {}".format(part2(pass_dict)))
