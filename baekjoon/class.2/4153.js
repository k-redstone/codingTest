// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let result = "";
for (let i = 0; i < input.length - 1; i++) {
  let arr = input[i].split(" ").sort((a, b) => {
    return a - b;
  });
  if (Math.pow(arr[0], 2) + Math.pow(arr[1], 2) == Math.pow([arr[2]], 2)) {
    result += "right" + "\n";
  } else {
    result += "wrong" + "\n";
  }
}

console.log(result);
