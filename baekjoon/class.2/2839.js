// let input = require("fs").readFileSync("/dev/stdin").toString();
let input = require("fs").readFileSync("data.txt").toString().trim();

let basket = 0;

while (input > 0) {
  if (input % 5 == 0) {
    input -= 5;
  } else {
    input -= 3;
  }
  basket++;
}

console.log(input == 0 ? basket : -1);
