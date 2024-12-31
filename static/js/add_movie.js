document.getElementById('Submit').addEventListener('click', function (event)
{
    event.preventDefault(); // Prevent default form submission

    const form = document.getElementById('addMovieForm');
    const formData = new FormData(form);

    fetch('/add_record_page', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        const messageDiv = document.getElementById('responseMessage');
        if (data.success) {
            messageDiv.textContent = data.message;
            messageDiv.style.color = 'green';
            form.reset(); // Clear the form fields
        } else {
            messageDiv.textContent = data.message;
            messageDiv.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error:', error);
        const messageDiv = document.getElementById('responseMessage');
        messageDiv.textContent = 'An error occurred while adding the movie.';
        messageDiv.style.color = 'red';
    });
});
