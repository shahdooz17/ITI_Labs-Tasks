function findLargest(num1, num2, num3) {
    if (num1 >= num2 && num1 >= num3) {
        return num1;
    } else if (num2 >= num1 && num2 >= num3) {
        return num2;
    } else {
        return num3;
    }
}


const num1 = parseFloat(prompt("Enter the first number:"));
const num2 = parseFloat(prompt("Enter the second number:"));
const num3 = parseFloat(prompt("Enter the third number:"));

const largestNumber = findLargest(num1, num2, num3);

console.log("Largest number:", largestNumber);
//-----------------------------------------------------------------------------------------------------
for (let i = 1; i <= 100; i++) {
    if (i === 10) {
        break;
    }
    console.log(i);
}
//-------------------------------------------------------------------------------------------------------
let i = 1;
while (i <= 100) {
    if (i === 10) {
        break;
    }
    console.log(i);
    i++;
}
//--------------------------------------------------------------------------------------------------------
for (let i = 1; i <= 100; i++) {
    if (i % 5 === 0) {
        continue;
    }
    console.log(i);
}
//----------------------------------------------------------------------------------------------------------
let j = 1;
while (j <= 100) {
    if (j % 5 !== 0) {
        console.log(j);
    }
    j++;
}

