/*
 * this script defers loading of the google map image until user is approxiamately
 * 300px away from reaching it. then it lazy loads it instantly.
 * improves loading speeds since itnow happens inthe background
 */

document.addEventListener("DOMContentLoaded", function () {
  const mapIframe = document.getElementById("googleMapIframe");
  if (!mapIframe) return;

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          // Assign src from data-src only when in range
          mapIframe.src = mapIframe.getAttribute("data-src");
          obs.disconnect(); // Stop observing once loaded
        }
      });
    },
    // Starts loading 300px before scrolling into view
    { rootMargin: "300px 0px" },
  );

  observer.observe(mapIframe);
});
