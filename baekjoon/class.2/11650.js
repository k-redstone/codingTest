// let input = fs.readFileSync("/dev/stdin").toString();
let [num, ...arr] = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

let newObj = [];

for (let i = 0; i < num; i++) {
  let sp = arr[i].split(" ");
  newObj.push({ x: sp[0], y: sp[1] });
}
newObj.sort((a, b) => a.x - b.x || a.y - b.y);

let result = "";
for (let i = 0; i < num; i++) {
  result += newObj[i].x + " " + newObj[i].y + "\n";
}

console.log(result);
