document.addEventListener('DOMContentLoaded', async function() {

 const url = 'http://127.0.0.1:8000/cours';

    try {
        
        const response = await fetch(url);
        const data = await response.json();
        window.events = data;

        console.log(events);
    } catch (error) {
        console.error('Error:', error);
        
    }

});