/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function (s) {
  const numberStack = []
  const stringStack = []
  let currentString = "";
  let k = 0;

  for (let i = 0; i < s.length; i++) {

      const char = s[i];
      if (!isNaN(s[i])) {
          //숫자 파싱
          k = k * 10 + Number(char);
      } else if (char === "[") {
        // 반복되는 문자열 시작, 그 전의 문자열은 stack에 저장해서 반복되는 것과 분리 
          stringStack.push(currentString);
          numberStack.push(k);
          currentString = "";
          k = 0;
      } else if (char === "]") {
        // 반복되는 문자열 끝, stack에서 pop해서 반복된 문자열을 currentString에 추가
          const repeatCount = numberStack.pop();
          const prevString = stringStack.pop();
          currentString = prevString + currentString.repeat(repeatCount);
      }
      else {
        //문자열인 경우 currentString에 추가
          currentString += char;
      }
  }
  return currentString
};