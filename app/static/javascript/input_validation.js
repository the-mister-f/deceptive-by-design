// Define regex for text and number inputs
const regexList = {
    name: /^[A-Za-z\s'-]+$/,  // Name validation regex
    age: /^\d+$/,  // Age validation regex (only numbers)
    email: /^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$/
};

// Define error messages for each field
const errorsList = {
    name: "Please enter a valid name",
    age: "Please enter a valid age",
    email: "Please enter a valid email",
    passwordMismatch: "Passwords do not match",
    passwordEmpty: "Password fields cannot be empty"
};

// Track whether the input has been interacted with
const inputTouched = {
    nameInput: false,
    ageInput: false,
    emailInput: false,
    passwordInput: false,
    repeatPasswordInput: false
};

// Check the validity of the input and enable/disable the "Next" button
function checkValidity(event) {
    const input = event.target;
    inputTouched[input.id] = true;  // Mark the input as touched
    validateInput(input);
}

// Validate input and update UI
function validateInput(input) {
    const inputID = input.id;
    const value = input.value;
    const errorMessageElement = document.getElementById('errorMessage');
    let regex, errorMessage;

    // Select the correct regex and error message based on input field
    switch (inputID) {
        case 'nameInput':
            regex = regexList.name;
            errorMessage = errorsList.name;
            break;
        case 'ageInput':
            regex = regexList.age;
            errorMessage = errorsList.age;
            break;
        case 'emailInput':
            regex = regexList.email;
            errorMessage = errorsList.email;
            break;
        default:
            validatePasswordFields();
            return;
    }

    if (!inputTouched[inputID]) {
        // If input has not been touched, skip validation
        input.style.borderColor = "var(--surfaces-border)"; // Reset border color
        errorMessageElement.classList.remove('show');
        disableButton(); // Assume invalid until touched
        return;
    }

    if (value === "") {
        // If input is empty
        input.style.borderColor = "red"; // Red border for empty input
        errorMessageElement.textContent = "This field is required";
        errorMessageElement.classList.add('show');
        disableButton(); // Disable button when input is invalid or empty
    } else if (regex.test(value)) {
        // If input is valid
        input.style.borderColor = "var(--surfaces-border)"; // Reset border color
        errorMessageElement.classList.remove('show');
        enableButton(); // Enable button when input is valid
    } else {
        // If input is invalid (does not match regex)
        input.style.borderColor = "red"; // Red border for invalid input
        errorMessageElement.textContent = errorMessage;
        errorMessageElement.classList.add('show');
        disableButton(); // Disable button when input is invalid
    }
}

// Validate password and repeated password fields
function validatePasswordFields() {
    const password = document.getElementById('passwordInput').value;
    const repeatPassword = document.getElementById('repeatPasswordInput').value;
    const errorMessageElement = document.getElementById('errorMessage');

    if (!inputTouched.passwordInput && !inputTouched.repeatPasswordInput) {
        errorMessageElement.classList.remove('show');
        return;
    }

    if (!password && !repeatPassword) {
        errorMessageElement.textContent = errorsList.passwordEmpty;
        errorMessageElement.classList.add('show');
        disableButton();
    } else if (password !== repeatPassword) {
        errorMessageElement.textContent = errorsList.passwordMismatch;
        errorMessageElement.classList.add('show');
        disableButton();
    } else {
        errorMessageElement.classList.remove('show');
        enableButton();
    }
}

// Handle Terms of Use toggle
function handleTermsOfUseToggle() {
    const termsToggle = document.getElementById('termsOfUseToggle');
    const requiredError = document.querySelector('.required-error');
    const nextButton = document.getElementById('next');

    if (termsToggle.checked) {
        requiredError.style.display = 'none'; // Hide required error
        enableButton();
    } else {
        requiredError.style.display = 'block'; // Show required error
        disableButton();
    }
}

// Handle radio button validation
function handleRadioValidation() {
    const radioButtons = document.querySelectorAll('input[type="radio"]');
    let isChecked = false;

    // Check if any radio button is selected
    radioButtons.forEach(radio => {
        if (radio.checked) {
            isChecked = true;
        }
    });

    // Enable or disable the "Next" button based on radio selection
    if (isChecked) {
        enableButton(); // Enable the "Next" button if a radio button is selected
    } else {
        disableButton(); // Disable the "Next" button if no radio button is selected
    }
}

// Function to disable the "Next" button
function disableButton() {
    const nextButton = document.getElementById('next');
    nextButton.disabled = true;
    nextButton.classList.add('disabled');
}

// Function to enable the "Next" button
function enableButton() {
    const nextButton = document.getElementById('next');
    nextButton.disabled = false;
    nextButton.classList.remove('disabled');
}

// Add event listeners to relevant input fields
document.querySelectorAll('input').forEach(input => {
    if (input.type === 'radio') {
        // For radio inputs, handle their state change
        input.addEventListener('change', handleRadioValidation); // Bind to radio's 'change' event
    } else {
        // For text/number inputs, bind 'input' event
        input.addEventListener('input', checkValidity);
    }
});

// Add event listener for Terms of Use toggle
document.getElementById('termsOfUseToggle').addEventListener('change', handleTermsOfUseToggle);


window.addEventListener('load', () => {
    let isAnyInputValid = false; // Flag to check if any input is valid

    // Check if the Terms of Use checkbox is checked by default and enable the button
    handleTermsOfUseToggle(); // Ensure that the checkbox state is checked

    // Validate all other inputs
    document.querySelectorAll('input').forEach(input => {
        if (input.type === 'radio') {
            handleRadioValidation();
            if (input.checked) {
                isAnyInputValid = true; // Set flag if any radio input is valid
            }
        } else {
            if (input.value.trim() !== "" && regexList[input.id.replace('Input', '')]?.test(input.value)) {
                isAnyInputValid = true; // Set flag if any input is valid
                inputTouched[input.id] = true; // Mark as touched if it has a valid value
            }
            validateInput(input);
        }
    });

    validatePasswordFields();

    // Enable/disable button based on form validation
    if (isAnyInputValid) {
        enableButton(); // Enable the "Next" button if any input is valid
    } else {
        disableButton(); // Otherwise, disable the "Next" button
    }
});

// Define the goBack function
function goBack() {
    window.history.back();
}