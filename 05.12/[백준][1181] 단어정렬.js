const fs = require('fs');
// TODO: 제출 시 경로 변환 필수 ("/dev/stdin")
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

// 풀이
function solution(input) {
  const N = Number(input[0]);
  const words = [...new Set(input.slice(1))];

  words.sort((a, b) => {
    if (a.length !== b.length) {
      return a.length - b.length
    }
    return a.localeCompare(b)
  })


  return words.join('\n');
}

console.log(solution(input));