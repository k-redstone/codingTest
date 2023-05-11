// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split(" ");

let star = "";

for (let i = 0; i < input[0]; i++) {
  for (let j = 0; j <= i; j++) {
    star += "*";
  }
  star += "\n";
}
console.log(star);
