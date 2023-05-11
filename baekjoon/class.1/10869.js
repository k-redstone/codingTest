// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let [one, two] = fs.readFileSync("data.txt").toString().trim().split(" ");

one = Number(one);
two = Number(two);
Math.floor();
console.log(one + two);
console.log(one - two);
console.log(one * two);
console.log(Math.floor(one / two));
console.log(one % two);
