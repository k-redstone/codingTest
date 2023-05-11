// let input = fs.readFileSync("/dev/stdin").toString();
const fs = require("fs");

let input = fs.readFileSync("data.txt").toString().trim().split("\n");

for (let i = 1; i < input.length; i++) {
  let score = input[i].toString().split("X");
  let totalScore = 0;
  score = score.filter((n) => n.length !== 0);
  for (let j = 0; j < score.length; j++) {
    for (let k = 1; k <= score[j].length; k++) {
      totalScore += k;
    }
  }

  console.log(totalScore);
}
