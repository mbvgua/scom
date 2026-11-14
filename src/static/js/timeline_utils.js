document.addEventListener("DOMContentLoaded", function () {
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
});
