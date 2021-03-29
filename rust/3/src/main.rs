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

fn toboggan(forest: &Vec<String>, vx: usize, vy: usize) -> u64 {
    let mut x = 0;
    let mut y = 0;
    let mut tree_count = 0;

    while y < forest.len() {
        if forest[y].chars().nth(x).unwrap() == '#' {
            tree_count += 1;
        }
        x = (x + vx) % forest[0].len();
        y += vy;
    }
    return tree_count
}

fn part1() -> u64{
    let input = read_input();
    if let Err(e) = &input {
        eprintln!("Error occured: {}", e);
        std::process::exit(1);
    }

    let forest = input.unwrap();

    let tree_count = toboggan(&forest, 3, 1);

    return tree_count;
}

fn part2() ->u64{
    let input = read_input();
    if let  Err(e) = &input {
        eprintln!("Error occured: {}", e);
        std::process::exit(1);
    }

    let forest = input.unwrap();

    let tree_results: Vec<u64> = vec![
        toboggan(&forest, 1, 1),
        toboggan(&forest, 3, 1),
        toboggan(&forest, 5, 1),
        toboggan(&forest, 7, 1),
        toboggan(&forest, 1, 2),
    ];

    let tree_count: u64 = tree_results.iter().fold(1, |acc, x| acc * x);

    return tree_count;
}

fn main() {
    let part1_result = part1();
    println!("The first answer is: {}", part1_result);
    let part2_result = part2();
    println!("The second answer is: {}", part2_result);
}
