// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const getPrime = (num) => {
  for (let j = 2; j * j <= num; j++) {
    if (num % j === 0) return false;
  }
  return true;
};

for (let i = input[0]; i <= input[1]; i++) {
  if (getPrime(i) == true && i !== 1) {
    console.log(i);
  }
}
