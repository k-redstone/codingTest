// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");
let result = [];
let obj = [];
let newArr = input.map((el) => el.split(" "));

for (let i = 1; i < newArr.length; i++) {
  obj.push({ id: i, name: newArr[i][1], age: newArr[i][0] });
}
obj = obj.sort((a, b) => a.age - b.age || a.id - b.id);

for (let j = 0; j < obj.length; j++) {
  result.push(obj[j].age + " " + obj[j].name);
}
console.log(result.join("\n"));
