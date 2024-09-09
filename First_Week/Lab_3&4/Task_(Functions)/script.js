function greet(name) { // Task_1 Greet a user
    console.log(`Hello, ${name}!`);
    }
    
    greet("Shahd"); // Example usage

    function addNumbers(num1, num2) { //Task_2 Add Two Numbers
        return num1 + num2;
        }
        const num1=prompt('Enter The First Number');
        const num2=prompt('Enter The Second Number');
    console.log(addNumbers(num1, num2)); // Example usage

    function factorial(number) { //Task_3 Factorial
        let result = 1;
        for (let i = 1; i <= number; i++) {
          result *= i;
        }
        return result;
    }
    const number = prompt('Enter the Number to get the factorial');
    console.log(factorial(number)); // Example usage

    function findMax(arr) { // Task_4 Find the maximum of an array
        let max = arr[0];
        for (let i = 1; i < arr.length; i++) {
            if (arr[i] > max) {
                max = arr[i];
            }
        }
        return max;
    }
    
    const input = prompt("Enter numbers separated by spaces:");
    const arr = input.split(' ').map(Number); 
    console.log(findMax(arr));

    function isPalindrome(str) { // Task_5 Palindrome
        let reversed = '';
        for (let i = str.length - 1; i >= 0; i--) {
            reversed += str[i];
        }
        return str === reversed;
    }
      console.log(isPalindrome("madam")); // Example usage