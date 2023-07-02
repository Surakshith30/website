console.log("form.js")

  var email = document.getElementById("exampleInputEmail2");
  var fname = document.getElementById("name");
  var phone = document.getElementById("number");
  var password1 = document.getElementById("comment");
  // var password2 = document.getElementById("pswd2");
  const form = document.querySelector('#form');
  // window.onload = function() {
  //     document.getElementById("form").reset();
  //   };
  
  // window.dataLayer = window.dataLayer || [];
  form.addEventListener('submit', (e) => {
   console.log("gg")
      if (!validateForm()) {       
          e.preventDefault();
      }
      else {
          e.preventDefault();
  
          analytics.track('form submitted', {
              name: fname.value,
              email: email.value,
          });
          form.dispatchEvent(new CustomEvent('form_submit'));
  
          dataLayer.splice(1,1,{
              'form': {
                  'name': "ggg",
                  'email': email.value
              }
          })
         
        
   
            
      }
  
  });
  
  // form.addEventListener('submit', (e) => {
  // window.location.href="help.html";
  // })
  // function thankyou(){
  //     console.log("yes");
  //     if (validateForm()) { 
  //     window.location.href="help.html";
  //     }
  // }
  function validateForm() {
      var email1 = email.value;
      var name1 = fname.value;
      var phone1 = phone.value;
      var password11 = password1.value;
      let success = true;
      if (email1 == "") {
          document.getElementById("message44").innerHTML = "email is required";
          success = false;
      } else {
          document.getElementById("message44").innerHTML = "";
      }
      if (!name1) {
          document.getElementById("message4").innerHTML = "Name is required";
          success = false;
      } else {
          document.getElementById("message4").innerHTML = "";
      }
  
      if (!phone1 || phone1.toString().length !== 10) {
          document.getElementById("message3").innerHTML = "Phone number is required";
          success = false;
      } else {
          document.getElementById("message3").innerHTML = "";
      }
  
      if (!password11) {
          document.getElementById("message1").innerHTML = "Password is required";
          success = false;
      } else {
          document.getElementById("message1").innerHTML = "";
      }
  
      return success;
  }
  
  