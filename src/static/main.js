// static/main.js

console.log("Sanity check!");

// Get Stripe publishable key
fetch("http://127.0.0.1:5000/payment/config")
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js
  const stripe = Stripe("pk_test_51MmIrBFHZFAE1pQVPrlMHKHZhwz9bhe0G3MObVgU0tZTDZWkzk1tQjWUCMfABMIsm8JLnWvR2Wb6P8dKKr66LITR009L64FDkh");

  // new
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/payment/create-checkout-session")
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});
