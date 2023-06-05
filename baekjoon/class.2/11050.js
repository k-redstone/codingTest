// let input = fs.readFileSync("/dev/stdin").toString();
let num = require("fs").readFileSync("data.txt").toString().trim().split(" ");

num = num.map(Number);
const calc = (num1, num2) => {
  let x = 1;
  let y = 1;
  for (let i = 1; i <= num2; i++) {
    x = x * num1;
    num1 -= 1;
  }
  for (let j = num2; j >= 1; j--) {
    y = y * j;
  }
  console.log(x / y);
};

calc(num[0], num[1]);
