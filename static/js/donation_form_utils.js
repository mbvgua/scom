document.addEventListener("DOMContentLoaded", function () {
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
