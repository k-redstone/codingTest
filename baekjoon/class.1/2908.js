// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split(" ");
const reversing = (str) => {
  return str.split("").reverse().join("");
};

console.log(Math.max(reversing(input[0]), reversing(input[1])));
