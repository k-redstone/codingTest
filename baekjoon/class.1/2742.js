// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim();

let result = [];
for (let i = input; i >= 1; i--) {
  result.push(i);
}
console.log(result.join("\n"));
