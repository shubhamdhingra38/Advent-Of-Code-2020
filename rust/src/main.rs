#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]

use std::cmp;
use std::collections::BinaryHeap;
use std::collections::HashMap;
use std::collections::HashSet;
use std::fs;
use std::io::stdin;
use std::time::{Duration, Instant};

#[derive(Default)] //initializes everything in struct with default value
struct Scanner {
    buffer: Vec<String>,
}
impl Scanner {
    fn next<T: std::str::FromStr>(&mut self) -> T {
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse::<T>().ok().expect("Failed parsing");
            } //otherwise buffer is empty or None, read another line and parse it
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed reading");
            let input = input.split_whitespace().rev();
            for token in input {
                self.buffer.push(token.to_string());
            }
        }
    }
    fn read_int(&mut self) -> i32 {
        self.next::<i32>()
    }
    fn read_bigint(&mut self) -> i64 {
        self.next::<i64>()
    }

    fn read_string(&mut self) -> String {
        self.next::<String>()
    }
    fn read_array(&mut self, n: i32) -> Vec<String> {
        let mut res = Vec::new();
        for _ in 0..n {
            res.push(self.read_string());
        }
        res
    }
    fn read_intarray(&mut self, n: i32) -> Vec<i32> {
        let mut res = Vec::new();
        for _ in 0..n {
            res.push(self.read_int());
        }
        res
    }
    fn read_bigarray(&mut self, n: i32) -> Vec<i64> {
        let mut res = Vec::new();
        for _ in 0..n {
            res.push(self.read_bigint());
        }
        res
    }
}



fn parse_rule(line: &str) -> (usize, Vec<&str>) {
    let mut element = line.split(":").into_iter();
    let rule_num = element.next().expect("error no next").parse::<usize>().expect("parse error");
    let rule = element.next().expect("error no next").split(" ");
    let mut rules = Vec::new();
    for r in rule {
        if r.len() != 0 {
            if r.starts_with("\"") {
                let r = r.strip_prefix("\"").unwrap().strip_suffix("\"").unwrap();
                rules.push(r);
            }
            else {
                rules.push(r);
            }
        }
    }

    println!("rule is {:?} with num {}", rules, rule_num);
    (rule_num, rules)
}

fn satisfies_rule(rule: &Vec<&str>, line: &str) -> bool{
    println!("checking if {} satisfy rule {:?}", line, rule);
    if rule.contains(&"|") {
        //a | b type
    }
    else {
        if rule.len() == 1 {
            assert_eq!(rule[0].len(), 1);
            let c = rule[0].chars().next().unwrap();
            
        }
    }
    true
}

fn is_valid_str(line: &str, rules: &HashMap<usize, Vec<&str>>) -> bool{
    println!("checking line: {}", line);

    let base_rule = rules.get(&0).unwrap();
    let mut i = 0;
    let mut string_idx = 0;
    while i < base_rule.len() {
        let ele = base_rule[i];
        match ele.parse::<usize>() {
            Ok(e) => {
                let rule = rules.get(&e).unwrap();
                if satisfies_rule(rule, &line[string_idx..]){
                    println!("YES!");
                    i += 1;
                }
                else {
                    return false;
                }
            },
            Err(err) => {panic!(err);}
        }
    }
    true
}

fn main() {
    // let mut scanner = Scanner::default();
    let now = Instant::now();
    let mut contents =
        fs::read_to_string("inp.txt").expect("Something went wrong reading the file");
    
    let splitted_itr = contents.split("\n").into_iter();

    let mut rules = HashMap::new();
    let mut processing_rules = true;
    let mut good_cnt = 0;
    for line in splitted_itr {
        if line.len()==0{
            //seperator, rules are now over
            processing_rules = false;
        }
        else {
            if processing_rules {
                let (x, y) = parse_rule(line);
                rules.insert(x, y);
            }
            else {
                //processing strings for validity
                if is_valid_str(line, &rules) {
                    good_cnt += 1;
                }
            }
        }
    }

    println!("{} time elapsed", now.elapsed().as_millis());
}

//reading causes strings to end with either \n or \n\r
fn trim_newline(s: &mut String) {
    if s.ends_with('\n') {
        s.pop();
        if s.ends_with('\r') {
            s.pop();
        }
    }
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        return a;
    }
    return gcd(b, a % b);
}
