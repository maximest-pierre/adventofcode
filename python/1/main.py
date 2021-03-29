
def part1(values):
    for i in range(0, len(values)):
        wanted_value = 2020 - values[i]
        print(wanted_value)
        if wanted_value in values:
            return (values[i] * wanted_value)

def part2(values):
    for i in range(0, len(values)):
        for j in range(i+1, len(values)):
            wanted_value = 2020 - values[i] - values[j]

            if wanted_value in values:
                return(values[i] * values[j] * wanted_value)

if __name__ == "__main__":
    # Open the file, read lines and strip the \n character
    with open('input') as file:
        values = file.readlines()
        values = [int(value[:len(value)-1]) for value in values]
    
    print("The first answer is: {}".format(part1(values)))
    print("The second answer is: {}".format(part2(values)))