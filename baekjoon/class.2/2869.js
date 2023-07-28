// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

let dayUp = input[0] - input[1];
if (dayUp === 1) {
  console.log(input[2] - input[0] + 1);
} else {
  console.log(Math.ceil((input[2] - input[0]) / dayUp) + 1);
}
