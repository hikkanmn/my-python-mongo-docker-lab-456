const form = document.querySelector("form");
const contact_name = document.getElementById("name");
const contact_surname = document.getElementById("surname");
const email = document.getElementById("email");

/*проверка почты при помощи регулярного выражения*/
function checkEmail() {
  const emailRegex = /^([a-z\d\.-]+)@([a-z\d-]+)\.([a-z]{2,3})(\.[a-z]{2,3})?$/;

  if (!email.value.match(emailRegex)) {
    email.classList.add("errorInput");
  } else {
    email.classList.remove("errorInput");
  }
}
/*проверка всех вводов (почты и сообщения)*/
function checkInputs() {
  if (contact_name.value == "") {
    contact_name.classList.add("errorInput");
  }

  if (contact_surname.value == "") {
    contact_surname.classList.add("errorInput");
  }

  if (email.value != "") {
    checkEmail();
  }

  email.addEventListener("keyup", () => {
    checkEmail();
  });

  contact_name.addEventListener("keyup", () => {
    if (contact_name.value != "") {
      contact_name.classList.remove("errorInput");
    } else {
      contact_name.classList.add("errorInput");
    }
  });

  contact_surname.addEventListener("keyup", () => {
    if (contact_surname.value != "") {
      contact_surname.classList.remove("errorInput");
    } else {
      contact_surname.classList.add("errorInput");
    }
  });
}

/*чтение клика по форме, применение проверок и отправка*/
form.addEventListener("submit", (e) => {
  checkInputs();
  if (
    !email.classList.contains("errorInput") &&
    !contact_name.classList.contains("errorInput") &&
    !contact_surname.classList.contains("errorInput")
  ) {
    
  }
  else {
    e.preventDefault();
    alert('Данные введены некорректно! Попробуйте снова')
  }
});