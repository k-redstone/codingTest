// let input = require("fs").readFileSync("/dev/stdin").toString();
let input = require("fs").readFileSync("data.txt").toString().trim();
let baseNum = 665;
let count = 0;

while (Number(count) !== Number(input)) {
  baseNum++;
  if (String(baseNum).includes("666")) {
    count += 1;
  }
}

console.log(baseNum);
