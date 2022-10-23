// cart_update
let cart_update = document.getElementsByClassName('.cart-update')
console.log(cart_update)

let url = "/cart_update/"
fetch(url)
    .then((response) => {
        console.log(response)
        return response.json
    })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })