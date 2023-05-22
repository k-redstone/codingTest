// push_front X: 정수 X를 덱의 앞에 넣는다.
// push_back X: 정수 X를 덱의 뒤에 넣는다.
// pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// size: 덱에 들어있는 정수의 개수를 출력한다.
// empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
// front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
// back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.

let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\r\n");

const stack = (type, num = 0) => {
  switch (type) {
    case "push_front":
      return stackArr.unshift(num);
    case "push_back":
      return stackArr.push(num);
    case "pop_front":
      if (stackArr.length == 0) {
        return "-1";
      } else {
        return stackArr.shift();
      }
    case "pop_back":
      if (stackArr.length == 0) {
        return "-1";
      } else {
        return stackArr.pop();
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
    case "size":
      return stackArr.length;
    case "empty":
      if (stackArr.length == 0) {
        return "1";
      } else {
        return "0";
      }
  }
};

let stackArr = [];
let result = [];
for (let i = 1; i < input.length; i++) {
  let base = input[i].split(" ");
  let im = stack(base[0], base[1]);
  if (base[0] !== "push_back" && base[0] !== "push_front") {
    result.push(im);
  }
}

console.log(result.join("\n"));
