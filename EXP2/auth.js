// Function to handle Login
document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    const res = await fetch("/login", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    if (res.ok) {
        // Save user session to browser memory
        localStorage.setItem("currentUser", JSON.stringify(data));
        window.location.href = "menu.html"; // Redirect to menu
    } else {
        alert(data.message);
    }
});

// Add your signup logic here similarly...