// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split(" ");

let input = require("fs").readFileSync("data.txt").toString().trim().split(" ");
let answer = BigInt(input[0]);
for (let i = 0; i < input[2]; i++) {
  answer = (answer * BigInt(input[1])) % BigInt(1000000007);
}
console.log(Number(answer));
// console.log((BigInt(input[0]) * num) % BigInt(1000000007));
