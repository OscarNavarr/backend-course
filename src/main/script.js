$(".choix_date input[type=date]").on('change', function(){
    $(".calendrier .selected_date").text(this.value.replace(/(\d+)-(\d+)-(\d+)/, "$3/$2/$1"));
});

// $.ajax(
//     {
//         // url: "http://127.0.0.1:8000/cours",
//         url: "/main.py",
//     }
// ).done(
//     function(data) {
//         console.log(data);
//     }
// );

fetch('http://localhost:32000/')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));