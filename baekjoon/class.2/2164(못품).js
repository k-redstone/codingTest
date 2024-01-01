// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs").readFileSync("data.txt").toString().trim();
let newArr = Array.from({ length: input }, (value, index) => index + 1);

let num = 0;
const methodShift = () => {
  if (newArr[newArr.length - 2] == 0) {
    return newArr[newArr.length - 1];
  } else {
    newArr[num] = 0;
    num += 1;
    methodMove();
  }
};
const methodMove = () => {
  if (newArr[newArr.length - 2] == 0) {
    return newArr[newArr.length - 1];
  } else {
    newArr.push(newArr[num]);
    newArr[num] = 0;
    num += 1;
    methodShift();
  }
};

methodShift();
console.log(newArr[num]);
