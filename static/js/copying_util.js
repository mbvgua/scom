document.addEventListener("DOMContentLoaded", function () {
  const copyButtons = document.querySelectorAll(".copy-btn");

  copyButtons.forEach(function (btn) {
    btn.addEventListener("click", async function () {
      // copy the data of previous element, which in this case is the
      // .account-value span, that has value to be copied
      const valueEl = btn.previousElementSibling;
      const textToCopy = valueEl.dataset.copyText;

      try {
        await navigator.clipboard.writeText(textToCopy);
        showCopiedState(btn);
      } catch (err) {
        // Fallback for older browsers / non-secure contexts
        fallbackCopy(textToCopy);
        showCopiedState(btn);
      }
    });
  });

  function showCopiedState(btn) {
    const icon = btn.querySelector("i");
    const originalClass = "bi-clipboard";
    const successClass = "bi-clipboard-check-fill";

    // change colors of icons to show copied successfully
    btn.classList.add("copied");
    icon.classList.remove(originalClass);
    icon.classList.add(successClass);

    // go to default after briefly showing copied success state
    setTimeout(function () {
      btn.classList.remove("copied");
      icon.classList.remove(successClass);
      icon.classList.add(originalClass);
    }, 1500);
  }

  function fallbackCopy(text) {
    const textarea = document.createElement("textarea");
    textarea.value = text;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();
    try {
      document.execCommand("copy");
    } catch (err) {
      console.error("Copy failed:", err);
    }
    document.body.removeChild(textarea);
  }
});
