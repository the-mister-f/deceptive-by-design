// Show Error message
document.addEventListener("DOMContentLoaded", function () {
    // Get references to the elements
    const smartBitesApp = document.getElementById("smartbites-app");
    const errorPopup = document.querySelector(".error-container");

    // Add a click listener to the document
    document.addEventListener("click", function (event) {
        // Check if the click was outside the smartBitesApp
        if (!smartBitesApp.contains(event.target)) {
            // Show the error popup
            errorPopup.style.display = "flex"; // Adjust display as needed (e.g., flex, block)
        } else {
            // Hide the error popup if the click is inside
            errorPopup.style.display = "none";
        }
    });
});

//Navigate to Appflow 3
window.onload = function () {
    const appIcon = document.querySelector('.app-icon');

    // Check if the current page is app_flow2
    if (window.location.pathname.includes('prototype02')) {
        // Wait for the animation to end before redirecting
        appIcon.addEventListener('animationend', function () {
            setTimeout(function () {
                console.log("eyoo");
                window.location.href = prototype03Url;
            }, 500);  // Short delay to ensure animation ends
        });
    }
};