async function checkPassword() {
  const password = document.getElementById("password").value;
  const res = await fetch("http://localhost:5000/check", {
    method: "POST",
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({ password })
  });

  const data = await res.json();
  const messages = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"];
  const colors = ["red", "orange", "gold", "green", "blue"];
  const widths = ["20%", "40%", "60%", "80%", "100%"];

  document.getElementById("result").innerText = `Score: ${messages[data.score]}, Breached: ${data.breached ? "Yes" : "No"}`;

  const bar = document.getElementById("strength-fill");
  bar.style.width = widths[data.score];
  bar.style.backgroundColor = colors[data.score];
}
