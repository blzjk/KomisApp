function carVisible(x) {
  var id = x;
  var div_search = document.getElementById("div_search")
  var div_panel = document.getElementById("div_panel")
  var buttonVisibleClassName = "";
  var buttonInvisibleClassName = "";
  if(div_search.className === "d-none"){
    buttonVisibleClassName = "visible_"
    buttonInvisibleClassName = "invisible_"
  }
  else {
    buttonVisibleClassName = "visible_search_"
    buttonInvisibleClassName = "invisible_search_"
  }
  var button = document.getElementById(buttonVisibleClassName + id);
  if(button === null){
  button = document.getElementById(buttonInvisibleClassName + id);
  }
  var xhr = new XMLHttpRequest();
  if (button.innerHTML === 'Widoczny') {
    xhr.open('POST', '/samochod_niewidoczny/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.innerHTML = 'Niewidoczny';
        button.className = 'btnHide btn btn-danger mt-1';

      }
      else {
        alert('Wystąpił błąd podczas ukrywania samochodu');
      }
    };
    xhr.send();
  }
  else {
    xhr.open('POST', '/samochod_widoczny/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.innerHTML = 'Widoczny';
        button.className = 'btnVisible btn btn-success mt-1';

      }
      else {
        alert('Wystąpił błąd podczas włączania widoczności samochodu');
      }
    };
    xhr.send();
  }
}

function carReservation(x) {
  var id = x;
  var buttonReservationClassName = "";
  var buttonEndReservationClassName = "";
  if(div_search.className === "d-none"){
    buttonReservationClassName = "reservation_"
    buttonEndReservationClassName = "end_reservation_"
  }
  else {
    buttonReservationClassName = "reservation_search_"
    buttonEndReservationClassName = "end_reservation_search_"
  }
  var button = document.getElementById(buttonReservationClassName + id);

  if(button === null){
  button = document.getElementById(buttonEndReservationClassName + id);
  }
  var xhr = new XMLHttpRequest();
  if (button.className === 'btnNotBook btn btn-secondary mt-1') {
    //tworzenie listy
        let highEnd = 30;
        let lowEnd = 0;
        var arr = [];
        c = highEnd - lowEnd + 1;
        while ( c-- ) {
         arr[c] = highEnd--
        }
 Swal.fire({
      title: 'Na ile dni chcesz wynająć pojazd?',
      input: 'select',

      inputOptions: arr,
      inputPlaceholder: 'Wybierz ilość dni',
      showCancelButton: true,
      cancelButtonText: 'Anuluj',
      confirmButtonText: 'Zatwierdź',
      allowOutsideClick: () => !Swal.isLoading()
    }).then((result) => {
      if (result.isConfirmed) {

        var count = result.value;
        xhr.open('POST', '/rezerwacja/'+id);
        xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
        xhr.onload = function() {
          if (xhr.status === 200) {
            button.innerHTML = 'Rezerwacja';
            button.className = 'btnBook btn btn-danger mt-1';
          }
          else {
            alert('Wystąpił błąd podczas procesu rezerwacji samochodu');
          }
        };
        xhr.send(`count_days=${count}`);
        }
    })
    }
  else {
    xhr.open('POST', '/koniec_rezerwacji/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.innerHTML = 'Zarezerwuj';
        button.className = 'btnNotBook btn btn-secondary mt-1';
      }
      else {
        alert('Wystąpił błąd podczas odwoływania rezerwacji samochodu');
      }
    };
    xhr.send();
  }
}

function carRent(x) {
  var id = x;
  var buttonEndRentClassName = "";
  if(div_search.className === "d-none"){
    buttonEndRentClassName = "end_rent_"
  }
  else {
    buttonEndRentClassName = "end_rent_search_"
  }
  button = document.getElementById(buttonEndRentClassName + id);
  var xhr = new XMLHttpRequest();
  if (button.className === 'btnHide btn btn-danger mt-1 col') {
    xhr.open('POST', '/koniec_wynajmu/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.className = 'btnBook btn btn-secondary mt-1';
        Swal.fire({
          title: 'Info',
          text: 'Wynajem został zakończony!',
          icon: 'info',
          confirmButtonText: 'OK'
          })
      }
      else {
        alert('Wystąpił błąd podczas zakończenia wynajmu');
      }
    };
    xhr.send();
  }
}

function searchVisible() {
  var button = document.getElementById("search_button");
  var div_search = document.getElementById("div_search")
  var div_panel = document.getElementById("div_panel")
  var xhr = new XMLHttpRequest();
  if (button.className == 'btn btn-primary') {
    xhr.open('POST', '/wyszukiwarka_panel_off/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        div_search.className = "d-none";
        div_panel.className = "";
        button.className = 'btn btn-secondary';
        button.innerHTML = 'Pokaż wyszukiwarkę';
      }
      else {
        alert('Wystąpił błąd podczas wyłączania wyszukiwarki');
      }
    };
    xhr.send();
  }
  else {
    xhr.open('POST', '/wyszukiwarka_panel_on/');
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        div_search.className = "";
        div_panel.className = "d-none";
        button.className = 'btn btn-primary';
        button.innerHTML = 'Ukryj wyszukiwarkę';
      }
      else {
        alert('Wystąpił błąd podczas włączania wyszukiwarki');
      }
    };
    xhr.send();
  }
}

document.addEventListener('DOMContentLoaded', setClassDiv(), false);

function setClassDiv(){
    var button = document.getElementById("search_button");
    var div_search = document.getElementById("div_search")
    var div_panel = document.getElementById("div_panel")
    if(button.className === "btn btn-secondary"){
        if(div_search != null) div_search.className = "d-none";
        if(div_panel != null) div_panel.className = "";
    }
    else {
        if(div_search != null) div_search.className = "";
        if(div_panel != null) div_panel.className = "d-none";
    }
}

function saveChanges(x){
    var id = x;
    var input_price_className = "";
    var input_description_className = "";
    var input_price_rent_className = "";
    if(div_search.className === "d-none"){
        input_price_className = "price_"
        input_price_rent_className = "price_rent_"
        input_description_className = "description_"
        }
    else {
        input_price_className = "price_search_"
        input_price_rent_className = "price_rent_search_"
        input_description_className = "description_search_"
    }
    var xhr = new XMLHttpRequest();
    var str = document.getElementById(input_price_className + id);
    if(str !== null){
        var input_price = parseFloat(str.value.replace(',','').replace(' ',''));
    }
    else {
        var input_price = 0;
    }

    var str_rent = document.getElementById(input_price_rent_className + id)
    if(str_rent !== null){
        var input_price_rent = parseFloat(str_rent.value.replace(',','.').replace(' ',''));
    }
    else {
        var input_price_rent = 0;
    }

    var input_description = document.getElementById(input_description_className + id).value;

    xhr.open('POST', '/zapisz/'+ id, true);
    xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    xhr.onreadystatechange = () => { // Call a function when the state changes.
      if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
          Swal.fire({
          title: 'Sukces!',
          text: 'Twoje zmiany zostały zapisane!',
          icon: 'success',
          confirmButtonText: 'OK'
          })
      }
    }
    xhr.send(`price=${input_price}&price_rent=${input_price_rent}&description=${input_description}`);
}
