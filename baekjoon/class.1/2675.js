// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");

for (let i = 1; i <= input[0]; i++) {
  let answer = "";
  let [a, b] = input[i].split(" ");
  for (let j = 0; j < b.length; j++) {
    answer += b[j].repeat(a);
  }
  console.log(answer);
}
