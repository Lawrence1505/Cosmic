function login() {
  let email = document.getElementById("email").value;
  let password = document.getElementById("password").value;

  fetch("/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password })
  })
  .then(response => response.json())
  .then(data => alert(data.message))
  .catch(error => console.error("Error:", error));
}

function register() {
  let email = document.getElementById("reg_email").value;
  let password = document.getElementById("reg_password").value;

  fetch("/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ email: email, password: password })
  })
  .then(response => response.json())
  .then(data => alert(data.message))
  .catch(error => console.error("Error:", error));
}
