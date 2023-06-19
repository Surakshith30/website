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
    'url': window.location.href
  });

//dataLayer
document.dispatchEvent(new CustomEvent('pageview'));
window.appEventData.splice(0,0,{
  'event': 'pageview',
  'pageName': resource,
  pageURL : window.location.href
              
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
      "pageURL" : window.location.href
                  
    });
    console.log("test kurma");

    
    window.appEventData.splice(0,0,{
      'event': 'pageview',
      'pageName': resource,
      "pageURL" : window.location.href
                  
    });
    
  }

});

getSession().then((emailId) => {
  let email1 = emailId ;
  let displayEmail = document.querySelector("#email");
displayEmail.textContent = email1;
});
console.log("getting");



document.addEventListener("click", function(event) {
  
  // Check if the clicked element is an anchor tag
  if (event.target.tagName === "A") {
    // Get the text of the clicked link
    var linkText = event.target.textContent;
    var linkurl=event.target.href
    
    event.preventDefault();
   
    // You can perform further actions with the link text here
    document.dispatchEvent(new CustomEvent("link_name", {detail: {'linkText':linkText,'linkurl':linkurl}}))
    window.location.href=event.target.href
  }
});