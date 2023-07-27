// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");
let answer = [];
let mode = [];
let max = 0;
let [numCount, ...arr] = input;
arr = arr.map(Number).sort((a, b) => {
  return a - b;
});
// 평균
answer.push(Math.round(arr.reduce((acc, cur) => acc + cur, 0) / numCount));
// 중간
answer.push(Math.round(arr[(numCount - 1) / 2]));
// 최빈
const map = new Map();
arr.reduce((acc, cur) => {
  map.has(cur) ? map.set(cur, map.get(cur) + 1) : map.set(cur, 1);
}, 0);

map.forEach((el, key) => {
  if (el > max) {
    mode = [];
    max = el;
    mode.push(key);
  } else if (max === map.get(key)) {
    mode.push(key);
  }
});
mode.length == 1
  ? answer.push(mode.sort((a, b) => a - b)[0])
  : answer.push(mode.sort((a, b) => a - b)[1]);
// 범위
answer.push(arr[numCount - 1] - arr[0]);

console.log(answer.join("\n"));
