function getGDC(a, b) {
  let gdc = 0;
  for (let i = 1; i <= Math.min(a, b); i += 1) {
    if (a % i === 0 && b % i === 0) {
      gdc = i;
    }
  }
  return gdc;
}

function getLCM(a, b) {
  return (a * b) / getGDC(a, b);
}

function solution(n, m) {
  var answer = [];
  const gdc = getGDC(n, m);
  const lcm = getLCM(n, m);
  answer.push(gdc);
  answer.push(lcm);
  return answer;
}