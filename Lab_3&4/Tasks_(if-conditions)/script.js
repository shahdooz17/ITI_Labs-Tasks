    function checkVotingEligibility(age) { // Task_1 Voting Eligiblity
        if (age >= 18) {
        console.log("You are eligible to vote.");
        } else {
        console.log("You are not eligible to vote.");
        }
    }
    const x = prompt("Enter Your Age Please");
    checkVotingEligibility(x);

    function compareNumbers(num1, num2) { // Task_2 cCompare Two Numbers
    if (num1 > num2) {
        console.log(`${num1} is larger.`);
    } else if (num2 > num1) {
        console.log(`${num2} is larger.`);
    } else {
        console.log("Both numbers are equal.");
    }
    }
    const num1 = prompt('Enter Your First Number');
    const num2 = prompt('Enter Your Second Number');
    compareNumbers(num1,num2); // Example usage

    function checkEvenOrOdd(number) {// Task_3 Check even or Odd
    if (number % 2 === 0) {
        console.log(`${number} is even.`);
    } else {
        console.log(`${number} is odd.`);
    }
    }
    const Num = prompt('Enter The Number To check');
    checkEvenOrOdd(Num); // Example usage

    function checkGrade(score) { // Task_4 Check Grade
    let grade;
    if (score >= 90) {
        grade = 'A';
    } else if (score >= 80) {
        grade = 'B';
    } else if (score >= 70) {
        grade = 'C';
    } else if (score >= 60) {
        grade = 'D';
    } else {
        grade = 'F';
    }
    console.log(`Your grade is ${grade}.`);
    }
    const grade = prompt('Enter Your Grade');
    checkGrade(grade); // Example usage


