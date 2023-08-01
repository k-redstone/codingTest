// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let [testSize, arr] = input;
arr = arr.split(" ").map(Number);
let answer = 0;

const getPrime = (num) => {
  for (let j = 2; j * j <= num; j++) {
    if (num % j === 0) return false;
  }
  return true;
};

for (let i = 0; i < testSize; i++) {
  if (getPrime(arr[i]) == true && arr[i] !== 1) {
    answer += 1;
  }
}
console.log(answer);
