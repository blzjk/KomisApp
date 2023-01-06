function carVisible(x) {
  var id = x;
  var button = document.getElementById("visible_" + id);
  if(button === null){
  button = document.getElementById("unvisible_" + id);
  }
  var xhr = new XMLHttpRequest();
  if (button.innerHTML == 'Widoczny') {
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
  var button = document.getElementById("reservation_" + id);
  if(button === null){
  button = document.getElementById("end_reservation_" + id);
  }
  var xhr = new XMLHttpRequest();
  if (button.className == 'btnNotBook btn btn-secondary mt-1') {
    xhr.open('POST', '/rezerwacja/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.className = 'btnBook btn btn-danger mt-1';
      }
      else {
        alert('Wystąpił błąd podczas ukrywania samochodu');
      }
    };
    xhr.send();
  }
  else {
    xhr.open('POST', '/koniec_rezerwacji/'+id);
    xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    xhr.onload = function() {
      if (xhr.status === 200) {
        button.className = 'btnNotBook btn btn-secondary mt-1';
      }
      else {
        alert('Wystąpił błąd podczas włączania widoczności samochodu');
      }
    };
    xhr.send();
  }
}
