// Check if user is logged in
const user = JSON.parse(localStorage.getItem("currentUser"));

if (!user) {
    window.location.href = "index.html"; // Boot them out if not logged in
} else {
    document.getElementById("welcomeUser").innerText = `Hi, ${user.name}`;
}

// Logout logic
document.getElementById("logoutBtn").addEventListener("click", () => {
    localStorage.removeItem("currentUser");
    window.location.href = "index.html";
});

// Load Orders and Add to Cart logic goes here (using user.email)