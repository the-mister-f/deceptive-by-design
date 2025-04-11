//Check Radio box by clicking its container
document.querySelectorAll('.radio-button').forEach((div) => {
    div.addEventListener('click', () => {
        const input = div.querySelector('input[type="radio"]');
        input.checked = true;
        input.dispatchEvent(new Event('change')); // Trigger a change event if needed
    });
});

// Dynamically assign values to radio buttons based on their labels
document.querySelectorAll('input[type="radio"]').forEach(radio => {
    const label = document.querySelector(`label[for="${radio.id}"]`);
    if (label) {
        radio.value = label.textContent.trim(); // Assign label text as the value
    }
});

// Add an event listener to the button
document.getElementById('showSelected').addEventListener('click', () => {
    // Get the selected radio button
    const selectedRadio = document.querySelector('input[type="radio"]:checked');

    // Get the label or display a message if none is selected
    const resultElement = document.getElementById('result');
    if (selectedRadio) {
        resultElement.textContent = `Selected label: ${selectedRadio.value}`;
    } else {
        resultElement.textContent = 'No option selected!';
    }
});

