// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim();

for (let i = 0; i < input[0]; i++) {
  let star = "";
  for (let j = input[0] - 1; j >= 0; j--) {
    star += j <= i ? "*" : " ";
  }
  console.log(star);
}
