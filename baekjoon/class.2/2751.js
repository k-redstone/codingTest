// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

input = input.slice(1).sort((a, b) => {
  return a - b;
});
console.log(input.join("\n"));
