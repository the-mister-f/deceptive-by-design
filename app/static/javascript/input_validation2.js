// Ensure the script runs after the DOM is fully loaded
document.addEventListener('DOMContentLoaded', function () {
    // Select the inputs and button
    const dateInput = document.getElementById('birthdayInput');
    const numberInput = document.getElementById('numberInput');
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    const submitButton = document.getElementById('next');

    // Function to enable the button
    function enableButton() {
        // Check if the date input is present and valid
        const dateValid = dateInput && dateInput.value.trim() !== "";
        // Check if the height input is present and valid
        const heightValid = numberInput && numberInput.value.trim() !== "" && !isNaN(numberInput.value) && numberInput.value > 0;
        // Check if at least one checkbox is checked
        const isAnyCheckboxChecked = Array.from(checkboxes).some(checkbox => checkbox.checked);

        // Enable the button if any of the conditions are true
        if (dateValid || heightValid || isAnyCheckboxChecked) {
            submitButton.disabled = false;
        } else {
            submitButton.disabled = true;
        }
    }

    // Add event listeners to all inputs
    if (dateInput) {
        dateInput.addEventListener('input', enableButton);
    }
    if (numberInput) {
        numberInput.addEventListener('input', enableButton);
    }
    if (checkboxes.length > 0) {
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', enableButton);
        });
    }

    // Call enableButton on page load to handle initial state
    enableButton();
});
