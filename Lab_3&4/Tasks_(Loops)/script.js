    for (let i = 1; i <= 10; i++) { // Tak_1 Print numbers from 1 to 10
        console.log(i);
    }

    let sum = 0;
    for (let i = 1; i <= 100; i++) { // Task_2 Print the sum of the numbvers from 1 to 100
        sum += i;
    }
    console.log(`The sum of numbers from 1 to 100 is ${sum}.`);

    function printMultiplicationTable(number) { //Task_3 Multiplication Table
        for (let i = 1; i <= 10; i++) {
          console.log(`${number} * ${i} = ${number * i}`);
        }
        }
    printMultiplicationTable(5); // Example usage

    function reverseString(str) { //Task_4 Reverse String
        let reversed = '';
        for (let i = str.length - 1; i >= 0; i--) {
            reversed += str[i];
            }
        console.log(`Reversed string: ${reversed}`);
        }
        
    reverseString("Hello"); // Example usage

        for (let i = 1; i <= 100; i++) { //Task_5 FizzBuzz
            if (i % 3 === 0 && i % 5 === 0) {
            console.log("FizzBuzz");
            } else if (i % 3 === 0) {
            console.log("Fizz");
            } else if (i % 5 === 0) {
            console.log("Buzz");
            } else {
            console.log(i);
            }
        }

