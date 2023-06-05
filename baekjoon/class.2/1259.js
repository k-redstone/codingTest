// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let check = false;
for (let i = 0; i < input.length - 1; i++) {
  let arr = input[i].split("");
  if (arr.length % 2 !== 0) {
    for (let j = 0; j < arr.length; j++) {
      if (arr[j] == arr[arr.length - i]) {
        check = true;
      }
    }
  } else {
    console.log("no");
  }
}
