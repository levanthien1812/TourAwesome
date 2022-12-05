const searchInput = document.querySelector('.search-tour-type')
const searchBtn = document.querySelector('.btn-search-tour')
const searchRecommend = document.querySelector('.search-tour-recommend')
let locationItems = document.querySelectorAll('.location-item')

searchInput.addEventListener('focus', () => {
    searchRecommend.classList.add('show')

    locationItems = Array.from(locationItems)
    locationItems.forEach(lctItem => {
        lctName = lctItem.querySelector('.name')
        lctItem.addEventListener('click', () => {
            console.log('Hello')
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


