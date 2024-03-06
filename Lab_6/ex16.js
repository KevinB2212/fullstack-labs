let person = {
    name: "Kevin Biju",
    age: 20,
    address: "DCU Dublin 9",
};

let x = {
    sayHello: function() {
        console.log('Hello, my name is ' + person.name);
    }
};

x.sayHello();