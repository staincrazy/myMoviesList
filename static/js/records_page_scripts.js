(function (){
    function recordsPageClean(){
        console.log('This script is executed')

        document.getElementById("Submit").addEventListener('click', clearTitleField)
        document.getElementById("Submit").addEventListener('click', clearDirectorNameField)
        document.getElementById("Submit").addEventListener('click', clearMovieRatingField)
    }

    function clearTitleField(){
        setTimeout(()=>{
            document.getElementById('movieTitle').value = ""
        }, 3000)

    }

    function clearDirectorNameField(){
        setTimeout(()=>{
            document.getElementById('directorName').value = ""
        }, 3000)

    }

    function clearMovieRatingField(){
        setTimeout(()=>{
            document.getElementById('movieRating').value = ""
        }, 3000)

    }

    recordsPageClean()
}())