

// this function is to get data from the backend
const getData = async (url) => {
    try {
        const response = await fetch(url);
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
};



document.addEventListener('DOMContentLoaded', async function() {

    // Get courses data
    const courses_url = 'http://127.0.0.1:8000/cours';
    const courses_data = await getData(courses_url);
    
    // Get teachers data
    const teachers_url = 'http://127.0.0.1:8000/enseignants';
    const teachers_data = await getData(teachers_url);

    // Get salles data
    const salles_url = 'http://127.0.0.1:8000/salles';
    const salles_data = await getData(salles_url);

    const all_data = [courses_data, teachers_data, salles_data];

    window.addDataToCalendar(all_data);
    

});