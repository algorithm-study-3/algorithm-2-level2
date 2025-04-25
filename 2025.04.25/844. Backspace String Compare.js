/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var backspaceCompare = function (s, t) {
  let sStack = [];
  let tStack = [];

  for (let i = 0; i < s.length; i++) {
    const char = s[i];
    if (char === '#') {
      sStack.pop();
    } else {
      sStack.push(char);
    }
  }

  for (let i = 0; i < t.length; i++) {
    const char = t[i];
    if (char === '#') {
      tStack.pop();
    } else {
      tStack.push(char);
    }
  }

  return JSON.stringify(sStack) === JSON.stringify(tStack);
};
