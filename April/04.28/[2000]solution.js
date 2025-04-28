var reversePrefix = function (word, ch) {
  // ch가 word에서 처음 나타나는 위치를 찾기
  const slicePosition = word.indexOf(ch);

  // ch가 word에 없으면 그대로 반환
  if (slicePosition === -1) return word;

  // ch까지 잘라서 뒤집기
  const reversedPrefix = word
    .slice(0, slicePosition + 1)
    .split("")
    .reverse()
    .join("");

  // 뒤집은 부분과 나머지 부분을 결합하여 반환
  return reversedPrefix + word.slice(slicePosition + 1);
};

// 동일하게 시간 복잡도는 O(n) 하지만, 배열로 해결하지 않아 불필요한 메모리 할당 없음
