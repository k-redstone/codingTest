// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\r\n");

let result = [];
let base1 = new Set(input[1].split(" "));
let base2 = input[3].split(" ");

for (let i = 0; i < input[2]; i++) {
  if (base1.has(base2[i])) {
    result.push(1);
  } else {
    result.push(0);
  }
}

console.log(result.join("\n"));

// set.has는 array.includes보다 빠르다
