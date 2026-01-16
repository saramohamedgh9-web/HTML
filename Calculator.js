// ===============================
// SIMPLE CALCULATOR LOGIC
// ===============================

const numbers = document.querySelectorAll(".number");
const operators = document.querySelectorAll(".operator");

const historyDisplay = document.getElementById("history");
const outputDisplay = document.getElementById("output");

let currentValue = "";
let previousValue = "";
let operator = "";

// ===============================
// NUMBER BUTTONS
// ===============================
numbers.forEach(button => {
  button.addEventListener("click", () => {
    currentValue += button.innerText;
    outputDisplay.innerText = currentValue;
  });
});

// ===============================
// OPERATOR BUTTONS
// ===============================
operators.forEach(button => {
  button.addEventListener("click", () => {
    const value = button.innerText;

    if (value === "C") {
      clearAll();
    }
    else if (value === "CE") {
      currentValue = currentValue.slice(0, -1);
      outputDisplay.innerText = currentValue;
    }
    else if (value === "=") {
      calculate();
    }
    else {
      setOperator(value);
    }
  });
});

// ===============================
// SET OPERATOR
// ===============================
function setOperator(op) {
  if (currentValue === "") return;

  previousValue = currentValue;
  operator = op;
  currentValue = "";

  historyDisplay.innerText = `${previousValue} ${operator}`;
}

// ===============================
// CALCULATE
// ===============================
function calculate() {
  const prev = parseFloat(previousValue);
  const current = parseFloat(currentValue);

  if (isNaN(prev) || isNaN(current)) return;

  let result;

  switch (operator) {
    case "+":
      result = prev + current;
      break;
    case "−":
      result = prev - current;
      break;
    case "×":
      result = prev * current;
      break;
    case "÷":
      result = prev / current;
      break;
    case "%":
      result = prev % current;
      break;
    default:
      return;
  }

  outputDisplay.innerText = result;
  historyDisplay.innerText = "";

  currentValue = result.toString();
  previousValue = "";
  operator = "";
}

// ===============================
// CLEAR ALL
// ===============================
function clearAll() {
  currentValue = "";
  previousValue = "";
  operator = "";
  historyDisplay.innerText = "";
  outputDisplay.innerText = "";
}
