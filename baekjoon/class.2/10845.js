// push X: 정수 X를 큐에 넣는 연산이다.
// pop: 큐에서 가장 앞에 있는 정수를 빼고, 그 수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// size: 큐에 들어있는 정수의 개수를 출력한다.
// empty: 큐가 비어있으면 1, 아니면 0을 출력한다.
// front: 큐의 가장 앞에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// back: 큐의 가장 뒤에 있는 정수를 출력한다. 만약 큐에 들어있는 정수가 없는 경우에는 -1을 출력한다.

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
        return stackArr.shift();
      }
    case "size":
      return stackArr.length;
    case "empty":
      if (stackArr.length == 0) {
        return "1";
      } else {
        return "0";
      }
    case "front":
      if (stackArr.length == 0) {
        return "-1";
      } else {
        return stackArr[0];
      }
    case "back":
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
