document.addEventListener('DOMContentLoaded', () => {
    document.querySelector('#submit').disabled = true;

    //ensure the user can't send empty username to the app
    document.querySelector('#tasks').onkeyup = () => {
        if (document.querySelector('#tasks').value.length > 0){
            document.querySelector('#submit').disabled = false;
        }
        else document.querySelector('#submit').disabled = true;
    }
    //load the current value of display_name
    document.querySelector('#submit').onclick = () => {
        //store the users name in local storage
        let username = document.querySelector('#tasks').value;
        localStorage.setItem('display_name', username);
    }
    return false;

});