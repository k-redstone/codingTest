// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");
let [testSize, ...newArr] = input;
let answer = "";
newArr = newArr.map((item) => item.split(" ").map(Number));
newArr.sort((a, b) => {
  if (a[1] !== b[1]) return a[1] - b[1];
  else return a[0] - b[0];
});

for (let i = 0; i < newArr.length; i++) {
  answer += newArr[i].join(" ") + "\n";
}

console.log(answer);
