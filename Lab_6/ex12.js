function printer(callback, num1, num2) {
    console.log(callback(num1, num2));
}

printer(function(num1, num2) {
    return num1 + num2;
}, 5, 7);