document.getElementById('login-form').addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Send the username and password to the backend for verification.
    fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username, password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Redirect the user to a dashboard or another secure page.
            window.location.href = 'dashboard.html';
        } else {
            // Display an error message to the user.
            alert('Invalid username or password.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        // Display an error message to the user.
        alert('An error occurred while logging in.');
    });
});