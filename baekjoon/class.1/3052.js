// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");
let input = fs.readFileSync("data.txt").toString().trim().split("\n");

let arr = [];
for (let i = 0; i < 10; i++) {
  arr.push(input[i] % 42);
}
const set = new Set(arr);

console.log([...set].length);
