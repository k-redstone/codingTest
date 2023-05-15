// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs
  .readFileSync("data.txt")
  .toString()
  .trim()
  .toUpperCase()
  .split("");

let answer = input.sort();

let count = []        
for(let i  = 0; i < answer.length; i++) {
  let str = answer[i]
  if(str == answer[i]){
    count += 1
    if (count > realCount) {}
  }
  if (){}
}
