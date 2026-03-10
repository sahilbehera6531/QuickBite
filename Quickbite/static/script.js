function validateForm() {

    let name = document.getElementById("name").value
    let email = document.getElementById("email").value
    let mobile = document.getElementById("mobile").value

    let emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/
    let mobilePattern = /^[0-9]{10}$/


    if (name.length < 3) {
        alert("Name must be at least 3 characters")
        return false
    }

    if (!email.match(emailPattern)) {
        alert("Invalid email address")
        return false
    }

    if (!mobile.match(mobilePattern)) {
        alert("Mobile number must be 10 digits")
        return false
    }

    return true
}



function addToCart(foodName, price) {

    let cart = JSON.parse(localStorage.getItem("cart")) || []

    let item = {
        name: foodName,
        price: price
    }

    cart.push(item)

    localStorage.setItem("cart", JSON.stringify(cart))

    alert(foodName + " added to cart!")

}