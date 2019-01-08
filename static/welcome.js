document.addEventListener('DOMContentLoaded', () => {

    // get the username from the local storage
    let username = localStorage.getItem('display_name');
    const p = document.createElement('p');
    p.innerHTML = `Hello ${username}! Welcome to flack`;
    document.querySelector('#welcome-div').appendChild(p);

    //I want to move the channel array to js..so js would handle the addition of channels and checking if it exists
  

    
});