// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs
  .readFileSync("data.txt")
  .toString()
  .trim()
  .toUpperCase()
  .split("");

let answer = input.sort();
let str = "";
let result = "";
let strObj = {};
let max = 0;

for (let i = 0; i < answer.length; i++) {
  let cunStr = answer[i];
  if (str == answer[i]) {
    count += 1;
    strObj[str] = count;
  } else {
    str = cunStr;
    count = 1;
    strObj[str] = count;
  }
}

for (let key in strObj) {
  if (strObj[key] == max) {
    max = strObj[key];
    result = "?";
  }
  if (strObj[key] > max) {
    max = strObj[key];
    result = key;
  }
}

console.log(result);
