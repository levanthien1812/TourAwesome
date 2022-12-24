const scrollToTopBtn = document.querySelector('.scroll-to-top-btn')

window.onscroll = () => {
    if (document.body.scrollTop >= 100 || document.documentElement.scrollTop >= 100) {
        scrollToTopBtn.classList.add('show')
    } else {
        scrollToTopBtn.classList.remove('show')
    }
}

scrollToTopBtn.addEventListener('click', () => {
    window.scrollTo({top: 0, behavior: 'smooth'})
})