const searchInput = document.querySelector('.search-tour-type')
const searchBtn = document.querySelector('.btn-search-tour')
const searchRecommend = document.querySelector('.search-tour-recommend')
let locationItems = document.querySelectorAll('.location-item')

searchInput.addEventListener('focus', () => {
    offsetBottom = searchInput.getBoundingClientRect().bottom
    searchRecommend.top = offsetBottom
    searchRecommend.classList.add('show')

    locationItems = Array.from(locationItems)
    locationItems.forEach(lctItem => {
        lctItem.addEventListener('click', () => {
            lctName = lctItem.querySelector('.name')
            searchInput.value = lctName.textContent
            setTimeout(() => searchBtn.form.submit(), 300) 
            
        })
    })
})

searchInput.addEventListener('blur', () => {
    setTimeout(() => {
        searchRecommend.classList.remove('show')
    }, 200)
})


