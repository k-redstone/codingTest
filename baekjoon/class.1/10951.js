// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");

for (let i = 0; i < input.length; i++) {
  let [a, b] = input[i].split(" ");
  console.log(Number(a) + Number(b));
}
