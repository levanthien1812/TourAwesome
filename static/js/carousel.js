const carouselBody = document.querySelector('.carousel .body')
var images = document.querySelectorAll('.carousel .body img')
const dots = document.querySelector('.dots')
const prevBtn = document.querySelector('.control.prev-btn')
const nextBtn = document.querySelector('.control.next-btn')

images = Array.from(images)

const fillDot = (index, isFill) => {
    if (isFill)
        document.querySelectorAll('.dots .dot')[index].classList.add('fill')
    else
        document.querySelectorAll('.dots .dot')[index].classList.remove('fill')
}

// Initialize body
var index = 0
images[index].classList.add('show')

// Generate dots
const countImages = images.length
for (i = 0; i < countImages; i++) {
    dots.innerHTML += `<div class = "dot"> </div>`
}

fillDot(index, true)

// Handle clicking prev button
prevBtn.addEventListener('click', () => {
    fillDot(index, false)
    images[index].classList.remove('show')
    index === 0 ? index = images.length - 1 : index--
    images[index].classList.add('show')
    fillDot(index, true)
})

// Handle clicking next button
nextBtn.addEventListener('click', () => {
    fillDot(index, false)
    images[index].classList.remove('show')
    index === images.length - 1 ? index = 0 : index++
    images[index].classList.add('show')
    fillDot(index, true)
})
