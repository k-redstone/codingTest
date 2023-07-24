// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

for (let i = 1; i < input.length; i++) {
  let hotel = input[i].split(" ");
  if (Number(hotel[2]) > Number(hotel[0])) {
    let x = Math.ceil(hotel[2] / hotel[0]);
    let y = hotel[2] % hotel[0];
    if (y === 0) {
      y = hotel[0];
    }
    if (x < 10) {
      x = "0" + x;
    }
    console.log(String(y) + String(x));
  } else {
    console.log(hotel[2] + "01");
  }
}
