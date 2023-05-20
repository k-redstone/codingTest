// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let base1 = input[1].split(" ");
let base2 = input[3].split(" ");
let result = [];
for (let i = 0; i < base2.length; i++) {
  result += base1.filter((a) => a == base2[i]).length + " ";
}

console.log(result);
