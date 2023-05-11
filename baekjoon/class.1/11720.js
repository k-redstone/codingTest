// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");

let answer = 0;
for (let i = 0; i < input[0]; i++) {
  answer += Number(input[1][i]);
}
console.log(answer);
