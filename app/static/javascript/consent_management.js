// Show "review individual" button when scrolling to the bottom
window.addEventListener("scroll", function () {
    const reviewIndividual = document.getElementById("reviewIndividual");

    // Check if the user has scrolled to the bottom
    const isBottom =
        window.innerHeight + window.scrollY >= document.documentElement.scrollHeight;

    if (isBottom) {
        reviewIndividual.classList.remove("hidden");

    } else {
        reviewIndividual.classList.add("hidden");
    }
});

// Handle "Accept All" button functionality
document.getElementById('acceptAll').addEventListener('click', (event) => {
    event.preventDefault(); // Prevent default form submission

    const toggles = document.querySelectorAll('.consent-container input[type="checkbox"]'); // All toggle checkboxes

    // Check if all toggles are already checked
    const allChecked = Array.from(toggles).every(toggle => toggle.checked);

    if (allChecked) {
        // If all toggles are already checked, submit the form immediately
        document.getElementById('account_consent').submit();
    } else {
        // If not all toggles are checked, check them all instantly
        toggles.forEach((toggle) => {
            toggle.checked = true; // Turn on the toggle
            const slider = toggle.nextElementSibling; // Access the slider element
            slider.style.transition = 'none'; // Remove transition for instant effect
            slider.offsetHeight; // Trigger reflow to apply the style change immediately
            slider.style.transition = '0.4s'; // Re-enable the transition for animation
        });

        // Wait for the transition to finish before submitting the form
        setTimeout(() => {
            document.getElementById('account_consent').submit();
        }, 400); // Delay of 0.4s to match the CSS transition duration
    }
});