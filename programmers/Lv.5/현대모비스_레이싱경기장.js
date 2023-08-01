function solution(heights) {
  let answer = 0;
  let num = 0;
  let n = heights.length;
  let h = Math.floor(heights.length / 2);
  let minMax = [];

  heights.sort((a, b) => a - b);

  if (heights.length % 2 === 0) {
    minMax[2] = heights[h] - heights[h - 1];
    // answer = heights[h] - heights[h - 1];
    for (let i = 0; i < h; i++) {
      // 배열의 앞이 뒤보다 먼저 ( 0, h , 1 , h+1 ...)
      if (i == 0) {
        minMax[0] = heights[h + i] - heights[i];
      } else {
        if (minMax[0] > heights[h + i - 1] - heights[i]) {
          minMax[0] = heights[h + i - 1] - heights[i];
        }
        if (h + i < n && minMax[0] > heights[h + i] - heights[i]) {
          minMax[0] = heights[h + i] - heights[i];
        }
      }

      // 배열의 뒤가 앞보다 먼저 ( h , 0 , h+1 , 1...)
      if (i == 0) {
        minMax[1] = heights[h + i] - heights[i];
        if (minMax[1] > heights[h + i + 1] - heights[i]) {
          minMax[1] = heights[h + i + 1] - heights[i];
        }
      } else {
        if (minMax[1] > heights[h + i] - heights[i]) {
          minMax[1] = heights[h + i] - heights[i];
        }
        if (h + i + 1 < n && minMax[1] > heights[h + i + 1] - heights[i]) {
          minMax[1] = heights[h + i + 1] - heights[i];
        }
      }
    }
  } else {
    num = heights[h];
    a = num - heights[h - 1];
    b = heights[h + 1] - num;
    if (a !== b) {
      a > b ? (minMax[2] = a) : (minMax[2] = b);
    }

    // 배열의 길이가 홀수인 경우

    // 배열의 뒤가 앞보다 먼저 ( h , 0 , h+1 , 1...)
    for (let i = 0; i < h; i++) {
      // 배열의 앞이 뒤보다 먼저 ( 0, h , 1 , h+1 ...)
      if (i == 0) {
        minMax[1] = heights[h + i] - heights[i];
        if (minMax[1] > heights[h + i + 1] - heights[i]) {
          minMax[1] = heights[h + i + 1] - heights[i];
        }
      } else {
        if (minMax[1] > heights[h + i] - heights[i]) {
          minMax[1] = heights[h + i] - heights[i];
        }
        if (h + i + 1 < n && minMax[1] > heights[h + i + 1] - heights[i]) {
          minMax[1] = heights[h + i + 1] - heights[i];
        }
      }
    }
    // 배열의 앞이 뒤보다 먼저 ( 0, h , 1 , h+1 ...)
    // 앞이 1개 더 많다.
    h++;
    for (let i = 0; i < h + 1; i++) {
      if (i == 0) {
        minMax[0] = heights[h + i] - heights[i];
      } else {
        if (minMax[0] > heights[h + i - 1] - heights[i]) {
          minMax[0] = heights[h + i - 1] - heights[i];
        }
        if (h + i < n && minMax[0] > heights[h + i] - heights[i]) {
          minMax[0] = heights[h + i] - heights[i];
        }
      }
    }
  }
  answer = Math.max(...minMax);
  return answer;
}

let heights = [9, 9, 9, 9, 30];
console.log(solution(heights));
