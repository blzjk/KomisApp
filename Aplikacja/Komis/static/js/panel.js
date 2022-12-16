


function updateModelValue(model, field, value) {
  // Pobranie aktualnego obiektu modelu
  alert("taki alert");
  let modelObject = model.get();

  // Zmiana wartości pola
  modelObject[field] = value;

  // Uaktualnienie obiektu modelu
  model.set(modelObject);
}

var model = Samochod.objects.get(pk=1)


$(document).ready(function() {
    $(".btnBook ").click(function(){
        updateModelValue(model, "rezerwacja", "false");
        alert("book");
    });
});


