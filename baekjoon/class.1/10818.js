// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");
let arr = input[1].split(" ");

const max = Math.max(...arr);
const min = Math.min(...arr);

console.log(`${min} ${max}`);
