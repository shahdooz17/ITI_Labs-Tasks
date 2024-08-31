function calculate(value) {
    const display = document.getElementById('display');
    const currentValue = display.value;
    const lastChar = currentValue.slice(-1);

    if (value === 'C') {
        display.value = '';
    } else if (value === '=') {
        try {
            if (isValidExpression(display.value)) {
                display.value = evaluateExpression(display.value);
            } else {
                display.value = 'Error';
            }
        } catch {
            display.value = 'Error';
        }
    } else {
        if (isOperator(value)) {
            if (isOperator(lastChar) || currentValue === '') {
                return;
            }
        } else if (value === '.') {
            const parts = currentValue.split(/[\+\-\*\/]/);
            if (parts[parts.length - 1].includes('.')) {
                return;
            }
        }
        display.value += value;
    }
}

function isOperator(char) {
    return ['+', '-', '*', '/'].includes(char);
}

function isValidExpression(expression) {
    // Ensure expression does not start with an operator except for '-'
    if (isOperator(expression[0]) && expression[0] !== '-') {
        return false;
    }

    // Ensure expression does not end with an operator
    if (isOperator(expression.slice(-1))) {
        return false;
    }

    // Ensure there are no consecutive operators
    if (/[\+\-\*\/]{2,}/.test(expression)) {
        return false;
    }

    // Ensure no division by zero
    if (/\/0(?![\d\.])/.test(expression)) {
        return false;
    }

    // Ensure no multiple decimals in any number
    const parts = expression.split(/[\+\-\*\/]/);
    for (const part of parts) {
        if ((part.match(/\./g) || []).length > 1) {
            return false;
        }
    }

    return true;
}

function evaluateExpression(expression) {
    const operators = expression.split(/[\d.]+/).filter(Boolean);
    const numbers = expression.split(/[^.\d]+/).map(Number);

    while (operators.length > 0) {
        const operator = operators.shift();
        const num1 = numbers.shift();
        const num2 = numbers.shift();

        let result;
        switch (operator) {
            case '+':
                result = num1 + num2;
                break;
            case '-':
                result = num1 - num2;
                break;
            case '*':
                result = num1 * num2;
                break;
            case '/':
                if (num2 === 0) {
                    throw new Error('Division by zero');
                }
                result = num1 / num2;
                break;
            default:
                throw new Error('Invalid operator');
        }

        numbers.unshift(result);
    }

    return numbers[0];
}
