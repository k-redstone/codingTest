// let input = require("fs").readFileSync("/dev/stdin").toString().trim();
let input = require("fs").readFileSync("data.txt").toString().trim();
let num = 1;
let fact = 1;
let include = "";

function My(input) {
  for (let i = 1; i <= input; i++) {
    num = BigInt(num) * BigInt(i);
  }
  include = num.toString().split("");
  for (let j = include.length - 1; j > 0; j--) {
    if (include[j] == "0" && include[j - 1] !== "0") {
      fact = Number(include.slice(j - 1).join(""));
      num = include.length - j;
      break;
    }
  }
  if (input < 5) num = 0;
  return num;
}

// console.log(num);

function Factorial(input) {
  let answer = 0;
  if (input === 0) answer;
  for (let i = 1; i <= input; i++) {
    if (i % 5 === 0) answer++;
    if (i % 25 === 0) answer++;
    if (i % 125 === 0) answer++;
  }
  return answer;
}

console.log(Factorial(input));
console.log(My(input));
