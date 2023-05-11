// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split(" ");

const a = parseInt(input[0]);
const b = parseInt(input[1]);

if (a !== b) {
  if (a > b) {
    console.log(">");
  } else {
    console.log("<");
  }
} else {
  console.log("==");
}
