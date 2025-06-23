async function checkPassword() {
    const password = document.getElementById("password").value;
    const res = await fetch("http://localhost:5000/check", {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ password })
    });
    const data = await res.json();
    const messages = [
        "Very Weak", "Weak", "Moderate", "Strong", "Very Strong"
    ];
    document.getElementById("result").innerText = 
        `Score: ${messages[data.score]}, Breached: ${data.breached ? "Yes" : "No"}`;
}
