document.getElementById("registration-form").addEventListener("submit", function (e) {
    const userId = document.getElementById("user_id").value;
    const password = document.getElementById("password").value;

    // Simple front-end validation
    if (userId === "" || password === "") {
        alert("Please fill in all fields");
        e.preventDefault(); // Prevent form submission
    }
});
