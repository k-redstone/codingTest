// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

// console.log(input[1]);
newArr = [];

let ne = input.map((el) => el.split(" "));

console.log(ne[1][1]);
