// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const testSize = input.shift();
console.log(input.sort((a, b) => a - b).join("\n"));