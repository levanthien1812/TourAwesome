let deleteBtns = document.querySelectorAll('.delete-btn')
const cover = document.querySelector(".cover")

deleteBtns = Array.from(deleteBtns)

let confirmDeleteModal

deleteBtns.forEach(deleteBtn => {
    deleteBtn.addEventListener("click", e => {
        confirmDeleteModal = deleteBtn.nextElementSibling
        confirmDeleteModal.classList.add("show")
        cover.classList.add("show")

        const cancelBtn = confirmDeleteModal.querySelector('.cancel-btn')
        cancelBtn.addEventListener('click', e => {
            e.preventDefault()
            cover.click()
        })

        cover.addEventListener("click", () => {
            confirmDeleteModal.classList.remove("show")
            cover.classList.remove("show")
        });
    });
})