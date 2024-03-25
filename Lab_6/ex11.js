function add(num1, num2) {
    return num1 + num2;
}

function printer (callback, num1, num2) {
    console.log(callback(num1, num2));
}

printer(add, 10, 5);