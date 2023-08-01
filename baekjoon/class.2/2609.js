// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);
let num = 1;
input = input.sort((a, b) => a - b);

let a = input[1];
let b = input[0];
while (num !== 0) {
  num = a % b;
  a = b;
  b = num;
}

console.log(a);
console.log((input[0] / a) * (input[1] / a) * a);
