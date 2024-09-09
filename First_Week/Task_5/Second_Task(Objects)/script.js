const person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    getFullName: function() {
        return `${this.firstName} ${this.lastName}`;
    }
};

console.log(person.getFullName());

const car = {};

// Adding properties
car.make = 'Toyota';
car.model = 'Corolla';
car.year = 2021;
delete car.year;
console.log(car);

const library = {
    books: [
        { title: 'Book One', author: 'Author One', isAvailable: true },
        { title: 'Book Two', author: 'Author Two', isAvailable: false },
        { title: 'Book Three', author: 'Author Three', isAvailable: true }
    ]
};

console.log(library.books);

const calculator = {
    add: function(a, b) {
        return a + b;
    },
    subtract: function(a, b) {
        return a - b;
    },
    multiply: function(a, b) {
        return a * b;
    },
    divide: function(a, b) {
        return a / b;
    }
};

// Example usage:
console.log(calculator.add(5, 3)); // 8
console.log(calculator.divide(10, 2)); // 5


const student = {
    name: 'Alice',
    grades: [90, 85, 88],
    addGrade: function(newGrade) {
        this.grades.push(newGrade);
    }
};
student.addGrade(92);
console.log(student.grades);

