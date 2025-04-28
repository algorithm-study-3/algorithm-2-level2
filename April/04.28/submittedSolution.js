// 2000. Reverse Prefix of Word

/**
 * @param {string} word
 * @param {character} ch
 * @return {string}
 */
var reversePrefix = function (word, ch) {
  // ch가 word에서 처음 나타나는 위치를 찾기
  const slicePosition = word.split("").findIndex((word) => word === ch);
  // word에서 그 부분까지 잘라서 뒤집기
  const wordArray = word.slice(0, slicePosition + 1).split("");
  const leftWordArray = word.slice(slicePosition + 1).split("");
  const reversedWordArray = wordArray.reverse();
  // 나머지 부분이랑 join 하기
  const finalArray = wordArray.concat(leftWordArray);
  return finalArray.join("");
};
