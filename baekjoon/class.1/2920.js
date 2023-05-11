// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim();

const answer = {
  "1 2 3 4 5 6 7 8": "ascending",
  "8 7 6 5 4 3 2 1": "descending",
}[input];

console.log(answer || "mixed");
