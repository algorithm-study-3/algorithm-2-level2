function solution(arr1, arr2) {
    const answer = Array.from({ length: arr1.length }, (_, i) => Array(arr1[i].length).fill(0));

    arr1.forEach((line, idx1) => {
        line.forEach((n, idx2) => {
            answer[idx1][idx2] = n + arr2[idx1][idx2];
        })
    })

    return answer;
}