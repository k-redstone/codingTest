// push X: 정수 X를 스택에 넣는 연산이다.
// pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// size: 스택에 들어있는 정수의 개수를 출력한다.
// empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
// top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

// let input = fs.readFileSync("/dev/stdin").toString();
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");

const stack = (type, num = 0) => {
  switch (type) {
    case "push":
      return stackArr.push(num);
    case "pop":
      if (stackArr.length == 0) {
        return "-1";
      } else {
        return stackArr.pop();
      }
    case "size":
      return stackArr.length;
    case "empty":
      if (stackArr.length == 0) {
        return "1";
      } else {
        return "0";
      }
    case "top":
      if (stackArr.length == 0) {
        return "-1";
      } else {
        return stackArr[stackArr.length - 1];
      }
  }
};

let stackArr = [];
let result = [];
for (let i = 1; i < input.length; i++) {
  let base = input[i].split(" ");
  let im = stack(base[0], base[1]);
  if (base[0] != "push") {
    result.push(im);
  }
}

console.log(result.join("\n"));
