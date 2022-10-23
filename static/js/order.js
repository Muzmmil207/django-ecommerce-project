// cart_update
let cart_update = document.getElementsByClassName('.cart-update')
console.log(cart_update)

let url = "http://127.0.0.1:8000/cart_update/"
fetch(url)
    .then((respon) => {
        console.log(respon)
        return respon.json
    })
    .then((data) => {
        console.log('data: ', data)
        location.reload()
    })