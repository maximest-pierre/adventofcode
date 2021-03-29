use std::fs::File;
use std::io;
use std::io::{BufRead, BufReader};

fn read_input() -> Result<Vec<String>, io::Error> {
    let filename = "input";

    let file = File::open(filename)?;

    let reader = BufReader::new(file);
    let input: Vec<String> = reader.lines().collect::<Result<_, _>>().unwrap();

    Ok(input)
}

fn parse_line(line: &str) -> (usize, usize, char, &str) {
    let splitted_line: Vec<&str> = line.split([' ', ':', '-'].as_ref()).collect();
    let first_integer = splitted_line[0].parse::<usize>().unwrap();
    let second_integer = splitted_line[1].parse::<usize>().unwrap();
    let character = splitted_line[2].chars().nth(0).unwrap();
    let password = splitted_line[4];

    return (first_integer, second_integer, character, password);
}

fn part_1() -> i32 {
    let input = read_input();
    if let Err(e) = &input {
        eprintln!("Error occured: {}", e);
        std::process::exit(1);
    }
    
    let mut ok_count = 0;
    for line in input.unwrap().iter() {
        let (min, max, character, password) = parse_line(line);
        let count = password.chars().filter(|&c| c == character).count();
        
        if min <= count && count <= max {
            ok_count += 1;
        }
    }
    return ok_count;
}

fn part_2() -> i32 {
    let input = read_input();

    if let Err(e) = &input {
        eprintln!("Error occured: {}", e);
        std::process::exit(1);
    }

    let mut ok_count = 0;
    for line in input.unwrap().iter() {
        let (position1, position2, character, password) = parse_line(line);
        if (password.chars().nth(position1 - 1).unwrap() == character) 
            != (password.chars().nth(position2 - 1).unwrap() == character) {
                ok_count += 1;
            }
    }
    return ok_count;
}

fn main() {
    let part1_result = part_1();
    println!("The first answer is: {}", part1_result);
    let part2_result = part_2();
    println!("The second answer is: {}", part2_result);
}
