const btn = document.getElementById('Submit')

console.log('Before function');

btn.addEventListener("click", function ()

{
    console.log('inside function');
    setTimeout(function ()
    {

        const inputs = document.querySelectorAll('#movieTitle, #directorName, #movieRating')
        console.log(inputs.values());

        inputs.forEach(input=> {
            input.value = '';
        })
    }, 30)}


);
