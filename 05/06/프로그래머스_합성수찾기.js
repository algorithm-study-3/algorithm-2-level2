function solution(n) {
	let arr = [];

	for (let i = 1; i <= n; i++) {
		for (let j = 2; j < i; j++) {
			if (i % j === 0) {
				arr.push(i);
			}
		}
	}
	return [...new Set(arr)].length;
}
