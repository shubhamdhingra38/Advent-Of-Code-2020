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

#[derive(Hash, Eq, PartialEq, Debug, Copy, Clone)]
struct Coordinate {
    x: i32,
    y: i32,
    z: i32,
    w: i32,
}
const deltas: [i32; 3] = [-1, 0, 1];

fn get_neighbor_active(c: &Coordinate, set: &HashSet<Coordinate>) -> i32 {
    let mut cnt = 0;
    let mut cc = 0;
    for dx in deltas.iter() {
        for dy in deltas.iter() {
            for dz in deltas.iter() {
                for dw in deltas.iter() {
                    if dx == dy && dx == dz && dx == dw && dx == &0 {
                        continue;
                    }
                    cc += 1;
                    if set.contains(&Coordinate {
                        x: c.x + dx,
                        y: c.y + dy,
                        z: c.z + dz,
                        w: c.w + dw,
                    }) {
                        cnt += 1
                    }
                }
            }
        }
    }
    // assert_eq!(cc, 26);
    cnt
}
fn becomes_active(c: &Coordinate, set: &HashSet<Coordinate>) -> bool {
    return get_neighbor_active(c, set) == 3;
}
fn stays_active(c: &Coordinate, set: &HashSet<Coordinate>) -> bool {
    let r = get_neighbor_active(c, set);
    return r == 2 || r == 3;
}

fn solve(set: &mut HashSet<Coordinate>) {
    for _ in 0..6 {
        //six cycles
        println!("{} now len", set.len());
        let mut original = HashSet::new();
        for &k in set.iter() {
            original.insert(k);
        }

        for ele in original.iter() {
            //all active elements
            for dx in deltas.iter() {
                for dy in deltas.iter() {
                    for dz in deltas.iter() {
                        for dw in deltas.iter() {
                            if dx == dy && dx == dz && dx == dw && dx == &0 {
                                continue;
                            }
                            let c = Coordinate {
                                x: ele.x + dx,
                                y: ele.y + dy,
                                z: ele.z + dz,
                                w: ele.w + dw,
                            };
                            if !original.contains(&c) {
                                if becomes_active(&c, &original) {
                                    set.insert(c); //can insert multiple times but goes one time only
                                }
                            }
                        }
                    }
                }
            }
            //check if it becomes inactive
            if !stays_active(ele, &original) {
                set.remove(ele);
            }
        }
    }

    println!("{}", set.len());
}

fn main() {
    // let mut scanner = Scanner::default();
    let now = Instant::now();
    let mut contents =
        fs::read_to_string("inp.txt").expect("Something went wrong reading the file");

    let mut map = HashSet::new();
    for (i, line) in contents.split("\n").enumerate() {
        for (j, chr) in line.chars().enumerate() {
            if chr == '#' {
                //active
                map.insert(Coordinate {
                    x: i as i32,
                    y: j as i32,
                    z: 0,
                    w: 0,
                });
            }
        }
    }

    solve(&mut map);
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
