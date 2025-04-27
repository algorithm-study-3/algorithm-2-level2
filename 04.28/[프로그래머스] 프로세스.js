function solution(priorities, location) {
  const queue = priorities.map((priority, index) => { return { priority, index }; });
  let count = 0;

  while (queue.length > 0) {
    const maxPriority = Math.max(...queue.map(item => item.priority));
    const current = queue.shift();

    if (current.priority < maxPriority) {
      queue.push(current)
    } else {
      count += 1;
      if (current.index === location) {
        return count;
      }
    }
  }
}