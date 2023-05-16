// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");

const defaultScore = input[1].split(" ");
const maxScore = Math.max(...defaultScore);

let result = defaultScore.reduce((acc, cur) => {
  return (acc += (cur / maxScore) * 100);
}, 0);
console.log(result / input[0]);
