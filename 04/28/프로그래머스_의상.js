//해시

function solution(clothes) {
	let key = new Map();
	for (let i = 0; i < clothes.length; i++) {
		if (key.has(clothes[i][1])) {
			key.set(clothes[i][1], key.get(clothes[i][1]) + 1);
		} else {
			key.set(clothes[i][1], 1);
		}
	}
	let answer = 1;
	for (let a of key.values()) {
		answer *= a + 1;
	}

	return answer - 1;
}
