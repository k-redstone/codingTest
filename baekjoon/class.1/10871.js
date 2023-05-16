// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");
let input = fs.readFileSync("data.txt").toString().trim().split("\n");

let baseLine = input[0].split(" ");
let numArr = input[1].split(" ");
let result = numArr.filter((num) => num < Number(baseLine[1]));

console.log(result.join(" "));
