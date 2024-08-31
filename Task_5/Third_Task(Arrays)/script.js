const favoriteFoods = ['Pizza', 'Sushi', 'Ice Cream', 'Tacos', 'Pasta'];
console.log(favoriteFoods[2]); // Ice Cream

let numbers = [1, 2, 3, 4, 5];

// Push
numbers.push(6); // [1, 2, 3, 4, 5, 6]
// Pop
numbers.pop(); // [1, 2, 3, 4, 5]
// Shift
numbers.shift(); // [2, 3, 4, 5]
// Unshift
numbers.unshift(1); // [1, 2, 3, 4, 5]
console.log(numbers);

const numberArr = [1, 2, 3, 4, 5];

for (let i = 0; i < numberArr.length; i++) {
    console.log(numbers[i] * 2);
}
// Or using forEach
numberArr.forEach(num => console.log(num * 2));



function findLargestNumber(arr) {
    return Math.max(...arr);
}
const numbers_2 = [10, 20, 30, 40, 50];
console.log(findLargestNumber(numbers_2)); // 50


function removeDuplicates(arr) {
    return [...new Set(arr)];
}
const number= [1, 2, 2, 3, 4, 4, 5];
console.log(removeDuplicates(number)); // [1, 2, 3, 4, 5]

