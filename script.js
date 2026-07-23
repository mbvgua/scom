document.addEventListener("DOMContentLoaded", function () {
  const navbar = document.getElementById("mainNav");

  // Listen for scroll events on the window
  window.addEventListener("scroll", function () {
    if (window.scrollY > 50) {
      // User scrolled down -> add solid background & shrink
      navbar.classList.add("scrolled");
    } else {
      // User is at the top -> make transparent again
      navbar.classList.remove("scrolled");
    }
  });

  // year for the footer.updates automatically!
  const yearSpan = document.getElementById("current-year");
  if (yearSpan) {
    yearSpan.textContent = new Date().getFullYear();
  }

  // Select all timeline items with animation classes
  const timelineItems = document.querySelectorAll(
    ".fade-in-left, .fade-in-right",
  );

  // Create the observer
  const observer = new IntersectionObserver(
    (entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Add 'visible' class to trigger CSS animation
          entry.target.classList.add("visible");

          // Stop observing once it has faded in so it doesn't repeat
          observer.unobserve(entry.target);
        }
      });
    },
    {
      threshold: 0.3, // Triggers when 30% of the item is visible on screen
    },
  );

  // Attach observer to each item
  timelineItems.forEach((item) => {
    observer.observe(item);
  });

  // donation form
  const paymentSelect = document.getElementById("paymentMethod");
  const mpesaFields = document.getElementById("mpesaFields");
  const cardFields = document.getElementById("cardFields");
  const bankFields = document.getElementById("bankFields");

  paymentSelect.addEventListener("change", function () {
    // Hide all payment groups first
    mpesaFields.classList.add("d-none");
    cardFields.classList.add("d-none");
    bankFields.classList.add("d-none");

    // Show selected payment group
    switch (this.value) {
      case "mpesa":
        mpesaFields.classList.remove("d-none");
        break;
      case "card":
        cardFields.classList.remove("d-none");
        break;
      case "bank":
        bankFields.classList.remove("d-none");
        break;
    }
  });
});
