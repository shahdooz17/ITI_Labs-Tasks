const car = {
    model: "Toyota",
    year: 2020,
    color: "Red",
    startEngine: function() {
        return "Engine started";
    },
    stopEngine: function() {
        return "Engine stopped";
    }
};

// Print keys (attributes)
console.log("Keys:", Object.keys(car));

// Print values (attribute values)
console.log("Values:", Object.values(car));

// Print the entire object (attributes and their values)
console.log("Entire object:", car);
