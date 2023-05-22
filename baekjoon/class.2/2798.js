// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\r\n");

let dealer = input[0].split(" ");
let player = input[1].split(" ");
let result = 0;
for (let i = 0; i < dealer[0]; i++) {
  for (let j = i + 1; j < dealer[0]; j++) {
    for (let k = j + 1; k < dealer[0]; k++) {
      let num = Number(player[i]) + Number(player[j]) + Number(player[k]);
      if (num <= Number(dealer[1]) && num > result) result = num;
    }
  }
}
console.log(result);
