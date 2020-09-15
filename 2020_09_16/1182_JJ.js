//입력
const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const ns = input[0].split(' ');
const n = Number(ns[0]);
const s = Number(ns[1]);
const arr = input[1].split(' ').map( v => Number(v));


let ans = 0;

//브루드포스
function recursive(nowidx,sum,num){
    
    if(nowidx == n){
        if(sum == s && num>0)  ans = ans + 1;
        return;
    } 
    
    //끝내는 경우
    recursive(n,sum,num);

    //nowidx ~ n-1까지 돌기
    for(let i=nowidx;i<n;i=i+1) recursive(i+1,sum + arr[i],num+1);
}


recursive(0,0,0);

console.log(ans);