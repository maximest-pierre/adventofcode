def part1(rows):

    right_step, down_step = (3,1)

    trees_encounter = 0

    column = 0
    for row in rows:
        if row[column] == "#":
            trees_encounter += 1
        column = (column + right_step) % len(row)

    return trees_encounter

def part2(rows):

    slopes = [[1,1], [3, 1], [5, 1], [7,1], [1, 2]]
    result = 1

    for right, down in slopes:
        trees = 0
        column = 0
        row = 0

        while row < len(rows):
            if rows[row][column] == "#":
                trees += 1

            row += down
            column = (column + right) % len(rows[0])

        result *= trees

    return result

if __name__ == "__main__":
    # Open the file and readlines
    with open('input') as file:
        # convert lines into array and strip \n
        rows = [row.strip('\n') for row in file.readlines()]
    
    print("The first answer is: {}".format(part1(rows)))
    print("The second answer is: {}".format(part2(rows)))

