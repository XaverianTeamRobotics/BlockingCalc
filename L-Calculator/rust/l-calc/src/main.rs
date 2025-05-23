// L-Calculator ported from L-Calculator.py

use std::env;

const CLK: i32 = 1000;
const PI: f64 = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679;


struct Point {
    t: f64,
    l: f64,
    n: f64,
    blocked: bool,
}

impl Point {
    fn origin() -> Point {
        Point { t: 0.0, l: 0.0, n: 0.0, blocked: false }
    }

    // Another associated function, taking two arguments:
    fn new(t: f64, l: f64, n: f64, blocked: bool) -> Point {
        Point { t: t, l: l, n: n, blocked: blocked }
    }

    fn u(t: f64, l: f64, n: f64, blocked: bool) {
        if !blocked {
            let output: f64 = ((PI / n) * t + l).sin();
        } else {
            let output: f64 = ((PI / n) * t).sin();
        }
        return;
    }
}

struct Pair(Box<i32>, Box<i32>);

impl Pair {
    fn destroy(self) { // Don't know what to do with this 
        // Destructure `self`
        let Pair(first, second) = self;
        println!("Destroying Pair({}, {})", first, second);
        // First and Second escape scope and are freed
    }
}




fn main() {
    //println!("Hello, world!");
}
