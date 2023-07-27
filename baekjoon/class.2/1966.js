// 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.

// 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과,
// 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
// 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다.
// 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.

// let input = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
let input = require("fs")
  .readFileSync("data.txt")
  .toString()
  .trim()
  .split("\n");
let [n, ...arr] = input;
arr = arr.map((item) => item.split(" ").map(Number));

for (let i = 0; i < arr.length; i += 2) {
  let printList = arr[i + 1];
  let monitorQue = arr[i][1];
  let result = 0;
  let count = 0;
  while (printList.length > 0) {
    let critical = Math.max(...printList);
    if (printList[0] < critical) {
      if (monitorQue === 0) {
        monitorQue = printList.length - 1;
        printList.push(printList[0]);
        printList.shift();
      } else {
        printList.push(printList[0]);
        printList.shift();
        monitorQue -= 1;
      }
    } else {
      if (monitorQue === 0) {
        result = count + 1;
        break;
      } else {
        printList.shift();
        critical = Math.max(...printList);
        monitorQue -= 1;
        count += 1;
      }
    }
  }
  console.log(result);
}
