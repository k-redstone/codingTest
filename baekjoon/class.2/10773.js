// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

let newArr = [];
let answer = 0;
for (let i = 1; i <= input[0]; i++) {
  if (input[i] === 0) {
    newArr.pop();
  } else {
    newArr.push(input[i]);
  }
}
for (let i = 0; i < newArr.length; i++) {
  answer += newArr[i];
}
console.log(answer);
