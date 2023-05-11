// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().toUpperCase();

let answer = input.sort();

console.log(answer);
