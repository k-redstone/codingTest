const input = require("fs")
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./data.txt")
  .toString()
  .trim()
  .split("\n")
  .map((el) => el.split(" ").map(Number));

const T = parseInt(input[0]);

const d_row = [0, 0, -1, 1];
const d_col = [-1, 1, 0, 0];

let index = 1;

function solution() {
  let results = [];

  for (let t = 0; t < T; t++) {
    const [M, N, K] = input[index];
    index++;

    let matrix = Array.from(Array(N), () => Array(M).fill(0));
    for (let i = 0; i < K; i++) {
      const [col, row] = input[index];
      matrix[row][col] = 1;
      index++;
    }

    function BFS(row, col) {
      const queue = [[row, col]];
      matrix[row][col] = 2;

      while (queue.length) {
        const [c_row, c_col] = queue.shift();
        for (let d = 0; d < 4; d++) {
          const n_row = c_row + d_row[d];
          const n_col = c_col + d_col[d];

          if (n_row >= 0 && n_col >= 0 && n_row < N && n_col < M) {
            if (matrix[n_row][n_col] === 1) {
              matrix[n_row][n_col] = 2;
              queue.push([n_row, n_col]);
            }
          }
        }
      }
    }

    let count = 0;

    for (let row = 0; row < N; row++) {
      for (let col = 0; col < M; col++) {
        if (matrix[row][col] === 1) {
          BFS(row, col);
          count++;
        }
      }
    }
    results.push(count);
  }

  console.log(results.join("\n"));
}

solution();
