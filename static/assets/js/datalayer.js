// window.dataLayer = window.dataLayer || [];

// function getSession() {
//   return fetch("/get_session")
//       .then((response) => response.json())
//       .then((data) => data.email_id);
// }

// getSession().then((emailId) => {
//   if (emailId) {
//     window.dataLayer.push({'event': 'user_id',"user_id": emailId});
//   } else {
//     window.dataLayer.push({'event': 'user_id',"user_id": "anonymous"});
//   }
// });

var path = window.location.pathname;
var resource = path.replace(/\.html$/, "");
let url =window.location.href
digitalData = {
  page: {
     pageInfo: {
        'pageName': resource,
        pageURL : window.location.href
     }
  }
};
window.appEventData = window.appEventData||[];

const pageview = {
  'event': 'pageview',
  'pageName': resource,
  pageURL : window.location.href
              
};




// dataLayer.push({
//     'event': 'pageview',
//     'url': window.location.href
//   });
  
//   function addToCart(product_name1, product_image1, product_price1, product_id1){
//   let product = { 'product_id': product_id1, 
//   'product_name': product_name1, 
//   'product_image':product_image1,
//   'product_price': product_price1};
//   console.log ("here" , product);
//   dataLayer.push({'event':'Add to cart', product});
// }

window.dataLayer = window.dataLayer || [];

window.emailArray = [];
console.log(window.emailArray[0] ,"Array")
let emailuni = window.emailArray;
console.log("emailuni",emailuni[0])
let anon= "anonymous";
function getSession() {
  return fetch("/get_session")
      .then((response) => response.json())
      .then((data) => data.email_id);
}

function pushUserIdToDataLayer() {
  // if(window.emailArray.length > 0 ){
    window.dataLayer.push({'event': 'user_id',"user_id": window.emailArray[0]});
  // }
  // else{
  //   window.dataLayer.push({'event': 'user_id',"user_id": anon});
  // }
 //GTM dataLayer
  window.dataLayer.push({
    'event': 'pageview',
    'url': window.location.href,
  });

//dataLayer
document.dispatchEvent(new CustomEvent('pageview'));
window.appEventData.splice(0,0,{
  'event': 'pageview',
  'pageName': resource,
  'pageURL' : window.location.href,
  "user" : "logged in",
  deviceType,
  'email': window.emailArray[0]

              
});

  
//segment dataLayer
  analytics.identify( {
    email: window.emailArray[0]
  });
  console.log("test kurta");
  // var prodName = document.querySelector("h1.name").innerHTML;
  // console.log(prodName);

//   //query selector for product price
//   const parentElement = document.querySelector('.price-box');
//   const prodPrice = parentElement.querySelector('.price').innerHTML;
//   let newProdPrice = prodPrice.substring(1);
//   // prodPrice.innerHTML =newProdPrice;
//   console.log(newProdPrice);
//   // query selsector for  productId
//   const stockContainer = document.querySelector('.stock-container');
//   const stockId = stockContainer.querySelector('.value').textContent;
//   console.log(stockId); 
//   //query selector for  product category 
//   const ul = document.querySelector('div.breadcrumb-inner');
//   const secondListItem = ul.querySelectorAll('li')[1];
//   const clothingValue = secondListItem.textContent;

//   setDataLayerValues(prodName, newProdPrice, stockId, clothingValue, window.myEmail);

//   var prodName1 = document.querySelector(".product-name").innerHTML;
// 	console.log(prodName1);
//   //query selector for product price
// 	const parentElement2 = document.querySelector('.price-box');
// const prodPrice1 = parentElement2.querySelector('.price').innerHTML;
// let newProdPrice1 = prodPrice1.substring(1);
// console.log(newProdPrice1);

//   var prodId = document.querySelector(".product-id").innerHTML;
// 	console.log(prodId);

//   //query selector for  product category 
// const ul1 = document.querySelector('div.breadcrumb-inner');
// const secondListItem1 = ul1.querySelectorAll('li')[1];
// const clothingValue1 = secondListItem1 .textContent;
// console.log(clothingValue1);
// setDataLayerValues1(prodName1 ,newProdPrice1, prodId , clothingValue1 );
}



getSession().then((emailId) => {

  let email = emailId ;
  window.myEmail = email ;
  window.emailArray.push(emailId);

  console.log("Email ID: ", window.myEmail); // log the email ID to the console inside the function
  
  if(emailId){
    pushUserIdToDataLayer();
    
  }

  else
  {
    window.dataLayer.push({'event': 'user_id',"user_id": anon});

    window.dataLayer.push({
      'event': 'pageview',
      'url': window.location.href
    });

    
    document.dispatchEvent(new CustomEvent('pageview', {detail:{
    "pageName": resource,
    "pageURL" : window.location.href},
  }
  ));


  
    window.appEventData.splice(0,0,{
      'event': 'pageview',
      'pageName': resource,
      "pageURL" : window.location.href,
      "user" : "guest",
      deviceType
                  
    });
    console.log("test kurma");
    
    
    
  }

});
function getCookie(name) {
  const cookieString = document.cookie;
  const cookies = cookieString.split('; ');
  for (const cookie of cookies) {
      const [cookieName, cookieValue] = cookie.split('=');
      if (cookieName === name) {
          return decodeURIComponent(cookieValue); // Cookies are URL-encoded, so decode the value
      }
  }
  return null; // Return null if the cookie is not found
}
const cookie = getCookie('uuid');

getSession().then((emailId) => {
  let email1 = emailId ;
  let displayEmail = document.querySelector("#email");
displayEmail.textContent = email1;

// UUID setup
if (cookie) 
{console.log("cookie already exist")}

else {
function generateUUIDFromEmail(email) {
  const cryptoObj = window.crypto || window.msCrypto; // For older browsers compatibility
  if (cryptoObj && cryptoObj.getRandomValues) {
      const normalizedEmail = email.toLowerCase().trim();
      const buffer = new Uint8Array(16);
      cryptoObj.getRandomValues(buffer);

      // Create a hash from the normalized email using SHA-256
      const encoder = new TextEncoder();
      const data = encoder.encode(normalizedEmail);
      return  arrayToHex(buffer) + "  " +arrayToHex(data);
  } else {
      console.error('Your browser does not support secure random number generation.');
      return null;
  }
}

function arrayToHex(array) {
  return Array.from(array, byte => byte.toString(16).padStart(2, '0')).join('');
}

function setCookie(name, value, days) {
  const expirationDate = new Date();
  expirationDate.setTime(expirationDate.getTime() + (days * 24 * 60 * 60 * 1000));
  const expires = "expires=" + expirationDate.toUTCString();
  document.cookie = name + "=" + value + ";" + expires + ";path=/";
}

const email2 = email1; // Replace this with the desired email
console.log("Heyyy",email2);
const generatedUUID = generateUUIDFromEmail(email2);
if (generatedUUID) {
setCookie('uuid', generatedUUID, 30);
}
}});
console.log("getting");



document.addEventListener("click", function(event) {
  var linkText = event.target.textContent;
  var linkurl=event.target.href
  // Check if the clicked element is an anchor tag
  if (event.target.tagName === "A") {
    event.preventDefault();
    // Get the text of the clicked link
    
  linkText1.push(linkText) 
   
    // You can perform further actions with the link text here
    document.dispatchEvent(new CustomEvent("link_name", {detail: {'linkText':linkText,'linkurl':linkurl}}))
    window.appEventData.push(
      {
      'linkText':linkText,
      'linkurl':linkurl
    })

   
    
    window.location.href=event.target.href
  }
});


  var linkText1 = [] ;

var isMobile = /Mobi/i.test(navigator.userAgent);
var isTablet = /Tablet/i.test(navigator.userAgent);
var isDesktop = !isMobile && !isTablet;

if(isTablet==true){
  var deviceType="tablet"
  console.log(deviceType)
}
else if(isMobile==true){
  deviceType="Mobile"
  console.log(deviceType)
   
}else{
  deviceType="Desktop"
  console.log(deviceType)
}


      
   
