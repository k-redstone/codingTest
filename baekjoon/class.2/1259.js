// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");;
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\r\n");

let check = true;
let num = 0;
input.pop();

for (let i = 0; i < input.length; i++) {
  let test = input[i].split("");
  test.length % 2 === 0
    ? (num = test.length / 2)
    : (num = Math.floor(test.length / 2) + 1);
  for (let j = 0; j < num; j++) {
    test[j] === test[test.length - j - 1] ? (check = true) : (check = false);
    if (check === false) {
      break;
    }
  }
  if (check === false) {
    console.log("no");
  } else {
    console.log("yes");
  }
}
