function solution(progresses, speeds) {
  const result = [];
  const leftDays = progresses.map((progress, index) => Math.ceil((100 - progress) / speeds[index]));
  let maxLeftDays = leftDays[0];
  let nextDeploy = 0;

  result[nextDeploy] = 0;

  for (let i = 0; i < progresses.length; i += 1) {
    if (leftDays[i] <= maxLeftDays) {
      result[nextDeploy] += 1
    } else {
      maxLeftDays = leftDays[i];
      nextDeploy += 1;
      result[nextDeploy] = 1;
    }
  }
  return result;
}
