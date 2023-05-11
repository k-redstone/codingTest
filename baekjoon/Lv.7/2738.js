const fs = require("fs");

// const input = fs.readFileSync("/dev/stdin").toString().split("\n");
const input = fs.readFileSync("data.txt").toString().split("\n");

let [n, m] = input[0].split(" ");
let answer = "";

for (let i = 1; i <= n; i++) {
  let word1 = input[i].split(" ");
  let word2 = input[i + Number(n)].split(" ");
  for (let j = 0; j < m; j++) {
    let sum = Number(word1[j]) + Number(word2[j]);
    answer += sum + " ";
  }
  if (i != n) {
    answer += "\n";
  }
}

console.log(answer);
