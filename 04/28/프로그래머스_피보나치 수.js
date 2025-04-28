function solution(n) {
	let answer = 0;
	let result = [];

	for (let i = 0; i <= n; i++) {
		if (i == 0) result.push(0);
		if (i == 1) result.push(1);
		if (i >= 2) {
			let sum = result[i - 1] + result[i - 2];
			result.push(sum % 1234567);
		}
	}

	answer = result[n];
	return answer;
}
