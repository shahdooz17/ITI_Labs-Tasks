const counter = (function() {
    let count = 0;

    function updateDisplay() {
        document.getElementById('count').innerText = count;
    }

    return {
        increment: function() {
            count++;
            updateDisplay();
        },
        decrement: function() {
            count--;
            updateDisplay();
        },
        reset: function() {
            count = 0;
            updateDisplay();
        }
    };
})();

function increment() {
    counter.increment();
}

function decrement() {
    counter.decrement();
}

function reset() {
    counter.reset();
}
