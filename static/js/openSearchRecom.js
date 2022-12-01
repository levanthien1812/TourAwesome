const searchInput = document.querySelector('.search-tour-type')
const searchRecommend = document.querySelector('.search-tour-recommend')
searchInput.addEventListener('focus', () => {
    searchRecommend.classList.add('show')
})
searchInput.addEventListener('blur', () => {
    searchRecommend.classList.remove('show')
})