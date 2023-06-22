(function (){
    function recordsPageClean(){
        console.log('This script is executed')
        document.getElementById("Submit").addEventListener('click', clearTitleField)
        document.getElementById("Submit").addEventListener('click', clearDirectorNameField)
        document.getElementById("Submit").addEventListener('click', clearMovieRatingField)
    }

    function clearTitleField(){
        document.getElementById('movieTitle').value = ""
    }

    function clearDirectorNameField(){
        document.getElementById('directorName').value = ""
    }

    function clearMovieRatingField(){
        document.getElementById('movieRating').value = ""
    }

    recordsPageClean()
}())