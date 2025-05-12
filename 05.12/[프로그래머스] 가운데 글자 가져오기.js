function solution(s) {
    var answer = '';
    if (s.length % 2 == 0) {
        let middle = Math.floor(s.length / 2);
        answer = s.slice(middle - 1, middle + 1);
    } else {
        let middle = Math.floor(s.length / 2);
        answer = s[middle];
    }
    return answer;
}