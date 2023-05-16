// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split(" ");

const transMin = Number(input[0] * 60) + Number(input[1]);

if (transMin < 45) {
  let result = transMin + 1440 - 45;
  console.log(Math.floor(result / 60), result % 60);
} else {
  let result = transMin - 45;
  console.log(Math.floor(result / 60), result % 60);
}
