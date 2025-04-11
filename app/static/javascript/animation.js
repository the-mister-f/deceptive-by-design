const progressCircle = document.querySelector(".circle-progress");
const percentageText = document.getElementById("percentage");
const radius = 85; // Radius of the circle
const circumference = 2 * Math.PI * radius; // Circumference of the circle

progressCircle.style.strokeDasharray = circumference;

let progress = 0;

function updateProgress() {
    if (progress <= 100) {
        const offset = circumference - (progress / 100) * circumference;
        progressCircle.style.strokeDashoffset = offset;
        percentageText.textContent = `${progress}%`;
        progress++;

        // Continue the animation
        setTimeout(updateProgress, 50);
    } else {
        // Navigate to prototype18 when animation is complete
        window.location.href = prototype18Url;
    }
}

// Start the progress animation
updateProgress();
