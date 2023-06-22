const btn = document.getElementById('Submit')

btn.addEventListener('click', function handleClick(event){

    event.preventDefault();

    const inputs = document.querySelectorAll('#movieTitle, #directorName, #movieRating')
    console.log(inputs.values());

    inputs.forEach(input=> {
        input.value = '';
    })
});