#![allow(dead_code)]
#![allow(unused_imports)]
#![allow(unused_variables)]

use std::io::stdin;
use std::cmp;
use std::collections::HashMap;
use std::collections::BinaryHeap;
use std::fs;
use std::time::{Duration, Instant};



#[derive(Default)] //initializes everything in struct with default value
struct Scanner{
    buffer: Vec<String>,
}
impl Scanner{
    fn next<T: std::str::FromStr>(&mut self) -> T{
        loop {
            if let Some(token) = self.buffer.pop() {
                return token.parse::<T>().ok().expect("Failed parsing");
            } //otherwise buffer is empty or None, read another line and parse it
            let mut input = String::new();
            stdin().read_line(&mut input).expect("Failed reading");
            let input = input.split_whitespace().rev();
            for token in input{
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
fn eval_helper(operands: &mut Vec::<i64>, operations: &mut Vec::<char>) -> i64 {
    operations.reverse();
    operands.reverse();

    println!("{:?}", operations);
    println!("{:?}", operands);

    let mut has_plus = false;
    for op in operations.iter() {
        if *op == '+' {
            has_plus = true;
            break;
        }
    }
    let mut res: i64 = 1;
    if !has_plus {
        while operands.len() != 0 {
            let first = operands.pop().unwrap();
            res *= first;
        }
    } else {
        println!("has a plus");
        let mut others = Vec::new();
        for i in 0..operands.len() {
            if i != operands.len() -1 && operations[i] == '+' {
                let prev = operands[i];
                let next = operands[i+1];
                operands[i+1] = prev + next;
            }
            else {
                others.push(operands[i]);
            }
        }
        println!("{:?} others", others);
        while others.len() != 0 {
            let first = others.pop().unwrap();
            res *= first;
        }
    }
    println!("{}", res);
    res
}

fn evalute_expression(s: &str) -> i64 {

    let mut operations = Vec::new();
    let mut operands = Vec::new();
    let mut res = 0;
    let mut itr = s.chars();
    let mut was_reading_int = false;
    let mut int_str = String::new();
    for c in itr {
        // println!("{:?}", operands);
        // println!("{:?}", operations);
        if !c.is_digit(10) {
            if was_reading_int {
                let num = int_str.parse::<i64>().expect("error parsing");
                int_str.clear();
                operands.push(num);
                was_reading_int = false;
            }
        }
        if c == '(' {
            operations.push(c);
        }
        else if c == ')' {
            int_str.clear();
            let mut v = Vec::new();
            let mut u = Vec::new();
            loop{
                let chr = operations.pop().expect("stack empty");
                if chr == '('{
                    let n1 = operands.pop().unwrap();
                    v.push(n1);
                    v.reverse(); u.reverse();
                    let num = eval_helper(&mut v, &mut u);
                    operands.push(num);
                    break;
                }
                else {
                    let n1 = operands.pop().unwrap();
                    v.push(n1);
                    u.push(chr);
                }
            }
            int_str.clear();
        }
        else if c == '+' || c == '*' {
            operations.push(c);
        }
        else if c.is_digit(10) {
            int_str.push(c);
            was_reading_int = true;
        }
    }
    if was_reading_int {
        let num = int_str.parse::<i64>().expect("error parsing");
        int_str.clear();
        operands.push(num);
        was_reading_int = false;
    }

 
    // println!("{} length of operands", operands.len());
    eval_helper(&mut operands, &mut operations)
}

fn main() {
    // let mut scanner = Scanner::default();
    let now = Instant::now();
    let mut contents = fs::read_to_string("inp.txt")
            .expect("Something went wrong reading the file");
        
    let mut splitted = contents.split("\n");
    let mut res: i64 = 0;    
    for line in splitted {
        res += evalute_expression(line);
    }
    println!("{}", res);
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

fn gcd(a: i64, b: i64) -> i64{
    if b == 0 {
        return a;
    }
    return gcd(b, a%b);
}