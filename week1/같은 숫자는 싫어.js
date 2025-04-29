function solution(arr)
{
    let lastNumber = -1;
    const answer = arr.map((num) => {
        if(num === lastNumber) return; 
        lastNumber = num;
        return num;
    }).filter((num) => num !== undefined)
    
    return answer;
}