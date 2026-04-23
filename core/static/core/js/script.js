document.addEventListener("DOMContentLoaded", function () {
    const counters = document.querySelectorAll(".count");

    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute("data-target")) || 0;
        let count = 0;

        if (target === 0) {
            counter.textContent = 0;
            return;
        }

        const step = Math.ceil(target / 40);

        const updateCounter = setInterval(() => {
            count += step;

            if (count >= target) {
                counter.textContent = target;
                clearInterval(updateCounter);
            } else {
                counter.textContent = count;
            }
        }, 30);
    });

    const cards = document.querySelectorAll(".fade-card");

    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.transition = "0.4s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, index * 100);
    });
});