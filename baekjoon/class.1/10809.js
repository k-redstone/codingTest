// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");
let input = fs.readFileSync("data.txt").toString().trim();

const result = [];

for (let i = 97; i <= 122; i++) {
  result.push(input.indexOf(String.fromCharCode(i)));
}

console.log(result.join(" "));
