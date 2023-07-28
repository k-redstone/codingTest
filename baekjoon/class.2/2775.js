// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n").map(Number);
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n")
  .map(Number);

const testSize = input.shift();

for (let i = 0; i < testSize; i++) {
  const arr = new Array(input[i * 2])
    .fill(0)
    .map(() => new Array(input[i * 2 + 1]));
  for (let x = 0; x < input[i * 2 + 1]; x++) {
    arr[0][x] = Number(x + 1);
  }

  if (arr.length !== 1) {
    for (let y = 1; y < input[i * 2]; y++) {
      arr[y - 1].reduce((acc, cur, idx) => {
        acc = acc + cur;
        arr[y][idx] = acc;
        return acc;
      }, 0);
    }
  }
  console.log(arr[input[i * 2] - 1].reduce((acc, cur) => acc + cur));
}
