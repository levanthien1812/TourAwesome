const bookTourBtn = document.querySelector(".tour-booking .book-btn button");
const detailBookingPopup = document.querySelector(".booking-detail");
const cover = document.querySelector(".cover");
const reviewCards = document.querySelectorAll(".review-card");
const addReviewRating = document.querySelector(".add-review .rating");
const ratingInput = document.querySelector(".add-review .rating-input");
const tourRatingStar = document.querySelector(".tour-rating .star")

// Handling booktour button: click button to open booking popup
bookTourBtn.addEventListener("click", () => {
    detailBookingPopup.classList.add("show");
    cover.classList.add("show");

    const priceEle = detailBookingPopup.querySelector(".prices .price span");
    const quantityEle = detailBookingPopup.querySelector("#quantity");
    const totalPriceEle = detailBookingPopup.querySelector("#total-price");

    totalPriceEle.value =
        parseFloat(quantityEle.value) * parseFloat(priceEle.textContent);

    quantityEle.addEventListener("input", () => {
        totalPriceEle.value =
            parseFloat(quantityEle.value) * parseFloat(priceEle.textContent);
        totalPriceEle.value = totalPriceEle.value;
    });
});

// Click cover layer to exit popup
cover.addEventListener("click", () => {
    detailBookingPopup.classList.remove("show");
    cover.classList.remove("show");
});

// Add reviewed rating stars
starPathHTML = `
    <path
      d="M316.9 18C311.6 7 300.4 0 288.1 0s-23.4 7-28.8 18L195 150.3 51.4 171.5c-12 1.8-22 10.2-25.7 21.7s-.7 24.2 7.9 32.7L137.8 329 113.2 474.7c-2 12 3 24.2 12.9 31.3s23 8 33.8 2.3l128.3-68.5 128.3 68.5c10.8 5.7 23.9 4.9 33.8-2.3s14.9-19.3 12.9-31.3L438.5 329 542.7 225.9c8.6-8.5 11.7-21.2 7.9-32.7s-13.7-19.9-25.7-21.7L381.2 150.3 316.9 18z"
    />
  `;
starHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"> 
          ${starPathHTML}
        </svg>`;
if (reviewCards) {
    Array.from(reviewCards).forEach((reviewCard) => {
        const ratingEle = reviewCard.querySelector(".rating");
        const rating = ratingEle.classList[1];
        let i;
        for (i = 0; i < rating; i++) {
            ratingEle.innerHTML += starHTML;
        }
    });
}


// Add stars to new review
unfilledStarPathHTML = `
    <path
      d="M287.9 0C297.1 0 305.5 5.25 309.5 13.52L378.1 154.8L531.4 177.5C540.4 178.8 547.8 185.1 550.7 193.7C553.5 202.4 551.2 211.9 544.8 218.2L433.6 328.4L459.9 483.9C461.4 492.9 457.7 502.1 450.2 507.4C442.8 512.7 432.1 513.4 424.9 509.1L287.9 435.9L150.1 509.1C142.9 513.4 133.1 512.7 125.6 507.4C118.2 502.1 114.5 492.9 115.1 483.9L142.2 328.4L31.11 218.2C24.65 211.9 22.36 202.4 25.2 193.7C28.03 185.1 35.5 178.8 44.49 177.5L197.7 154.8L266.3 13.52C270.4 5.249 278.7 0 287.9 0L287.9 0zM287.9 78.95L235.4 187.2C231.9 194.3 225.1 199.3 217.3 200.5L98.98 217.9L184.9 303C190.4 308.5 192.9 316.4 191.6 324.1L171.4 443.7L276.6 387.5C283.7 383.7 292.2 383.7 299.2 387.5L404.4 443.7L384.2 324.1C382.9 316.4 385.5 308.5 391 303L476.9 217.9L358.6 200.5C350.7 199.3 343.9 194.3 340.5 187.2L287.9 78.95z"
    />
  `
unfilledStarHTML = `
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512">
          ${unfilledStarPathHTML}
      </svg>
    `;
if (addReviewRating) {
    let fiveStars = "";
    for (let i = 0; i < 5; i++) fiveStars += unfilledStarHTML;
    addReviewRating.innerHTML = fiveStars;

    // Handling hovering unfill stars
    const addReviewRatingStars = document.querySelectorAll(
        ".add-review .rating > *"
    );
    Array.from(addReviewRatingStars).forEach((star, index) => {
        star.addEventListener("mouseenter", () => {
            for (let i = 0; i <= index; i++) {
                addReviewRatingStars[i].innerHTML = starPathHTML;
            }
        });
        star.addEventListener("click", () => {
            ratingInput.value = index + 1
            for (let i = 0; i <= index; i++) {
                addReviewRatingStars[i].innerHTML = starPathHTML;
            }
        });
        star.addEventListener("mouseleave", () => {
            for (let i = 0; i <= index; i++) {
                addReviewRatingStars[i].innerHTML = unfilledStarPathHTML;
            }
        });
    });
}

tourRatingStar.innerHTML += starHTML