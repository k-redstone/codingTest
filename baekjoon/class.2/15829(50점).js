// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let [testSize, arr] = input;
arr = arr.split("");

let pow = 1;

const answer = arr.reduce((acc, cur, idx) => {
  acc += ((cur.charCodeAt(0) - 96) * 31 ** idx) % 1234567891;
  return acc % 1234567891;
}, 0);
console.log(answer);
