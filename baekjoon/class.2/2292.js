// let input = Number(require("fs").readFileSync("/dev/stdin").toString().trim());
let input = Number(require("fs").readFileSync("data.txt").toString().trim());
let acc = 1;
let cur = 1;

if (input === 1) {
  console.log(1);
} else {
  while (input > acc) {
    acc += cur * 6;
    cur += 1;
  }
  console.log(cur);
}
