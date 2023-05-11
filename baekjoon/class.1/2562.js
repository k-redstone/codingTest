// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().split("\n").map(Number);

const answer = Math.max(...input);
const index = input.indexOf(answer);
console.log(answer);
console.log(index + 1);
