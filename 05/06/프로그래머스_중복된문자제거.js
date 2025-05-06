function solution(my_string) {
	var answer = Array.from(new Set(my_string.split(""))).join("");

	return answer;
}
