const contentDiv = document.querySelector('#content');
const navLinks = document.querySelectorAll('#sidebar a');

function loadPage(url) {
    fetch(url)
        .then(response => response.text())
        .then(html => {
            contentDiv.innerHTML = html;
        })
        .catch(error => console.error(error));
}

navLinks.forEach(link => {
    link.addEventListener('click', event => {
        event.preventDefault();
        loadPage(link.href);
    });
});

// Load the home page by default
loadPage('home.html');