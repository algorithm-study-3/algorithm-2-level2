function solution(num_list) {
    const doubleCount = num_list.filter((num) => num % 2 === 0).length
    const singleCount = num_list.filter((num) => num % 2 !== 0).length
    
    return [doubleCount, singleCount];
}