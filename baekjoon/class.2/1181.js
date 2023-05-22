// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\r\n")
  .slice(1);

input = new Set(input);
let result = [...input].sort(
  (a, b) => a.length - b.length || a.localeCompare(b)
);

console.log(result.join("\n"));
