$(document).ready(function(){
    const checkbox = document.getElementById('id_would_like')
    const dateInput = document.getElementById('id_assisted_in')
    if (checkbox.checked) {
        dateInput.value = ''
        dateInput.disabled = true
    } else {
        dateInput.disabled = false
    }
    checkbox.addEventListener('change', (e) => {
        if (checkbox.checked) {
            dateInput.value = ''
            dateInput.disabled = true
        } else {
            dateInput.disabled = false
        }
    })
    }
)