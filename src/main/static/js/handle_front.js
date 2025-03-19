// Function to get the date without the time
const getDate = (date) => date.split("T")[0];

// This function is to get the time without the date
const getTime = (date) => {
    let time= date.split("T")[1] // get the time part
    let cleanTime = time.split("+")[0] // remove the timezone
    return cleanTime
};

// Function to close the modal
const closeModal = () => { 
    document.getElementById("modal-container").classList.add("hidden"); 
}

// Function to find an element by ID in an array list
const findById = (list, id, indexId) => {
    return list.find(item => item[indexId] == id);
}

// This function adds the data to the calendar
window.addDataToCalendar = function(data) {
    console.log("data", data);

    const [courses_data, teachers_data, salles_data] = data;

    var calendarEl = document.getElementById('calendar');
    var calendar = new FullCalendar.Calendar(calendarEl, {
        initialView: 'timeGridWeek',
        events: courses_data.cours.map(element => {
            // Get real teacher and room data using the correct indexes
            let teacher = findById(teachers_data.enseignants, element[1], 3); // Teacher ID is in position 3
            let salle = findById(salles_data.salles, element[2], 0); // Room ID is at position 0

            return {
                title: element[8], // Course name
                start: element[3], // Start date and time
                end: getDate(element[3]) + "T" + element[9], // End date and time
                extendedProps: {
                    id: element[0],
                    teacherName: teacher ? teacher[0] : "Inconnu", // Name is in position 0
                    salleName: salle ? salle[2] : "Inconnue", // Room name is in position 2
                    startTime: getTime(element[3]).toString(),
                    endTime: element[9].split("+")[0].toString()
                }
            };
        }),
        selectable: true,
        eventClick: function(info) {
            let event = info.event.extendedProps;

            document.getElementById("modal-container").classList.remove("hidden");

            // Update the modal with the correct information using the IDs
            document.getElementById("modal-course-name").textContent = info.event.title;
            document.getElementById("modal-teacher-name").textContent = event.teacherName;
            document.getElementById("modal-room-name").textContent = event.salleName;
            document.getElementById("modal-start-time").textContent = event.startTime;
            document.getElementById("modal-end-time").textContent = event.endTime;
        }
    });

    calendar.render();
};
