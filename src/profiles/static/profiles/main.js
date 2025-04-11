console.log('hello my profile')

const avatarBox = document.getElementById('avatar-box')
const alertBox = document.getElementById('alert-box')
const profileForm = document.getElementById('profile-form')
const csrf = document.getElementsByName('csrfmiddlewaretoken')

const bioInput = document.getElementById('id_bio')
const avatarInput = document.getElementById('id_avatar')

profileForm.addEventListener('submit', e => {
    e.preventDefault()

    const formData = new FormData()
    formData.append('csrfmiddlewaretoken', csrf[0].value)
    formData.append('bio', bioInput.value)
    formData.append('avatar', avatarInput.files[0])

    $.ajax({
        type: 'POST',
        url: window.location.href,
        enctype: 'multipart/form-data',
        data: formData,
        processData: false,
        contentType: false,
        cache: false,
        success: function (response) {
            console.log(response)
            avatarBox.innerHTML = `
                <img src="${response.avatar}?t=${new Date().getTime()}" class="rounded" height="200px" width="auto" alt="${response.user}">
            `

            bioInput.value= response.bio
            handleAlerts('success','Your Profile Has Been Updated!')
        },
        error: function (error) {
            console.log('Error:', error)
            alertBox.innerHTML = `<div class="alert alert-danger" role="alert">
                Something went wrong. Please try again.
            </div>`
        }
    })
})
