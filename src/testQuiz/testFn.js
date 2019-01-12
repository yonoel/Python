// 测试默认参数
function fn (val,list=[]) {
    // push 返回数组长度
    let n = list.push()

    return n;
}

result1 = fn(1);
result2 = fn(2);
result3 = fn(3);
console.log("result is",result1,result2,result3)