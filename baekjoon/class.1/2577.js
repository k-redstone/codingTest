// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");
let calc = (input[0] * input[1] * input[2]).toString().split("");

let result = {
  0: 0,
  1: 0,
  2: 0,
  3: 0,
  4: 0,
  5: 0,
  6: 0,
  7: 0,
  8: 0,
  9: 0,
};

calc.map((el) => {
  result[el] += 1;
});

for (let i = 0; i < 10; i++) {
  console.log(result[i]);
}
