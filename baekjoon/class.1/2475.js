// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split(" ");

let result = input.reduce((acc, cur) => {
  return (acc += cur ** 2);
}, 0);
console.log(result % 10);
