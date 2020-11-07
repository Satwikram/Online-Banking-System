function validateSignup() {
  var x = document.forms["myform"]["psw"].value;
  var y = document.forms["myform"]["psw-repeat"].value;

  if (x != y) {
    alert("password missmatch!");
    return false;
  }
}

function validateLogin() {
            var ph = document.getElementById("ph").value;
            var password = document.getElementById("psw").value;
            if (ph == null || ph == "") {
                alert("Please enter the Phone Number.");
                return false;
            }
            if (password == null || password == "") {
                alert("Please enter the password.");
                return false;
            }
            alert('Login successful');

        }
