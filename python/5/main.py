with open("./input", "r") as file:
    boarding_passes = list(
        map(lambda boarding_pass: boarding_pass.strip("\n"), file.readlines())
    )
print(boarding_passes)