// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let base1 = input[1].split(" ");
let base2 = input[3].split(" ");
let resultArr = new Array(Number(input[2])).fill(0);
let filter = base1.reduce((accu, curr) => {
  accu[curr] = (accu[curr] || 0) + 1;
  return accu;
}, {});

for (let i = 0; i < base2.length; i++) {
  if (filter[base2[i]] !== undefined) {
    resultArr[i] = filter[base2[i]];
  }
}

console.log(resultArr.join(" "));
