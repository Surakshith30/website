const basket_num  = document.querySelector('#cart_num');
const basket_total_price  = document.querySelector('#cart_price');

let cart_product_number = 0;
let total_price = 0;
let added_products = {};
let quantity_prod = document.getElementById("Qty");
let quant;



function increaseQty() {
  var qty = document.getElementById("Qty");
  qty.value = parseInt(qty.value) + 1;
  }
  
  function decreaseQty() {
  var qty = document.getElementById("Qty");
  if (qty.value > 1) {
    qty.value = parseInt(qty.value) - 1;
  }
  }

  // let added_products1 = localStorage.getItem('added_products');
  // function addProductToCart() {
  //   fetch('/addProductToCart', {
  //     method: 'POST',
  //     body: JSON.stringify({ added_products1 }),
  //     headers: {
  //       'Content-Type': 'application/json'
  //     }
  //   })
  //   .then(response => response.json())
  //   .then(data => console.log(data))
  //   .catch(error => console.error(error));
  // }

    if(localStorage.getItem('cart_product_number') != null){
      cart_product_number = Number(localStorage.getItem('cart_product_number'));
      total_price = Number(localStorage.getItem('total_price'));  
      basket_num.innerText = cart_product_number;
      //total_price = Number(total_price).toFixed(2);
      basket_total_price.innerText = `$${Number(total_price).toFixed(2)}`;
    }

    if(localStorage.getItem('added_products') != null){
      added_products = localStorage.getItem('added_products');
      added_products = JSON.parse(added_products); //JSON.parse(JSON.parse(added_products));
      console.log('added_products', added_products);
      console.log('added_products keys', Object.keys(added_products));

    }


function addToCart(product_name, product_image, product_price, product_id){

  if(quantity_prod==undefined){
    quant = 1;
   
 }
 else{
  quant= quantity_prod.value ;
   console.log("kick");
 }
 

  let product = {
 'product_id': product_id, 'product_name': product_name, 'product_image': product_image, 'product_price': product_price, 'product_quantity':quant}
  console.log('Clicked on Add to Cart', product_name, product_image, product_price)


  console.log('added_products keys', Object.keys(added_products));

  if(Object.keys(added_products).find(element => element == product_id)){

  added_products[product_id].product_quantity = Number(added_products[product_id].product_quantity)+Number(quant);
  console.log('Added Product Quantity', added_products[product_id], added_products[product_id].product_quantity);

  }
  else{
  added_products[product_id] = product; 
  cart_product_number += 1;
  localStorage.setItem('cart_product_number', cart_product_number);

  }
  //added_products.push(product) ; 
  total_price += Number(product_price * quant); 

  
  localStorage.setItem('total_price', total_price);
  localStorage.setItem('added_products', JSON.stringify(added_products));

  // localStorage.setItem('product_image', product_image);
  // localStorage.setItem('product_price', product_price);

  basket_num.innerText = cart_product_number;
  basket_total_price.innerText = `$${total_price.toFixed(2)}`;
  console.log('added_products', added_products);
  alert('Product Added Successfully');
// dataLayer.push({'event':'Add To cart', 'product_id': product_id, 'product_name': product_name , 'product_price': product_price})
dataLayer.push({ ecommerce: null });  // Clear the previous ecommerce object.
dataLayer.push({
  'event': 'add_to_cart',
  'ecommerce': {
  'currencyCode': 'EUR',
    'items': [{                        //  adding a product to a shopping cart.
    'item_name': product_name ,
    'item_id': product_id,
    'price': product_price,
    'quantity': 1
     }]
  
  }
});

addProductToCart();
}

// function getSession() {
//   return fetch("/get_session")
//       .then((response) => response.json())
//       .then((data) => data.email_id);
// }

// getSession().then((emailId) => {
//   dataLayer.push({"user_id":emailId});
// });

// function getSession() {
//   return fetch("/get_session")
//       .then((response) => response.json())
//       .then((data) => data.email_id);
// }

// getSession().then((emailId) => {
//   if (emailId) {
//     window.dataLayer.push({"user_id": emailId});
//   } else {
//     window.dataLayer.push({"user_id": "anonymous"});
//   }
// });

const products = JSON.parse(localStorage.getItem('added_products'));
// Get the cart items list element
const cartItems = document.getElementById('cart_items');


function miniCart(){
let template = '';
Object.values(products).forEach(product => {
  // products.forEach((product) => {
 template  += `
  <li>
    <div class="cart-item product-summary">
      <div class="row">
        <div class="col-xs-4">
          <div class="image"> <a href="detail.html"><img src="${product.product_image}" alt="${product.product_name}"></a> </div>
        </div>
        <div class="col-xs-7">
          <h3 class="name"><a href="index8a95.html?page-detail">${product.product_name}</a></h3>
          <div class="price">${product.product_price}</div>
        </div>
        <div class="col-xs-1 action"> <a href="#"><i class="fa fa-trash"></i></a> </div>
      </div>
    </div>
  </li>
`
});
document.querySelector('#cart_items').innerHTML = template;
}

//  const myLink = querySelectorAll(".btn btn-primary")

// myLink.addEventListener('click', function() {
//   // event.preventDefault(); // prevent the link from navigating to a new page
//   miniCart(); // call your function here
// });

miniCart();

// window.onload.miniCart(); 

// document.addEventListener("DOMContentLoaded", function() {
  // miniCart();
// });


// function getSession() {
//   return fetch("/get_session")
//       .then((response) => response.json())
//       .then((data) => data.email_id);
// }

// getSession().then((emailId) => {
//   if (emailId) {
//     dataLayer.push({"user_id": emailId});
//   }
// });
  // const basket_num  = document.querySelector('#cart_num');
  // const basket_total_price  = document.querySelector('#cart_price');
  
  // let cart_product_number = 0;
  // let total_price = 0;
  // let added_products = { };

  // if(sessionStorage.getItem('cart_product_number') != null){
  //   cart_product_number = Number(sessionStorage.getItem('cart_product_number'));
  //   total_price = Number(sessionStorage.getItem('total_price'));  
  //   basket_num.innerText = cart_product_number;
  //   basket_total_price.innerText = `$${total_price}`;
  // }

  // if(sessionStorage.getItem('added_products') != null){
  //   added_products = sessionStorage.getItem('added_products');
  // }
  
  // function addToCart(product_name, product_image, product_price, product_id){

  //   let product = { 'product_name': product_name, 'product_image': product_image, 'product_price': product_price,'produc_id':product_id}

  //   console.log('Clicked on Add to Cart', product_name, product_image, product_price)
  //   cart_product_number += 1;
  //   total_price += Number(product_price);
  //   console.log("total_price", total_price,typeof(total_price));
  //   sessionStorage.setItem('cart_product_number', cart_product_number);
  //   sessionStorage.setItem('total_price', total_price);

  //   pname = `product${cart_product_number}`;

  //   added_products[pname] = product; 
    
  //   sessionStorage.setItem('added_products', added_products);
  //   // sessionStorage.setItem('product_image', product_image);
  //   // sessionStorage.setItem('product_price', product_price);

  //   basket_num.innerText = cart_product_number;
  //   basket_total_price.innerText = `$${total_price.toFixed()}`;

  // }

  // const basket_num  = document.querySelector('#cart_num');
  // const basket_total_price  = document.querySelector('#cart_price');
  
  // let cart_product_number = 0;
  // let total_price = 0;
  // let added_products = {};

  // if(localStorage.getItem('cart_product_number') != null){
  //   cart_product_number = Number(localStorage.getItem('cart_product_number'));
  //   total_price = Number(localStorage.getItem('total_price'));  
  //   basket_num.innerText = cart_product_number;
  //   //total_price = Number(total_price).toFixed(2);
  //   basket_total_price.innerText = `$${Number(total_price).toFixed(2)}`;
  // }

  // if(localStorage.getItem('added_products') != null){
  //   added_products = localStorage.getItem('added_products');
  //   added_products = JSON.parse(added_products); //JSON.parse(JSON.parse(added_products));
  //   console.log('added_products', added_products);
  //   console.log('added_products keys', Object.keys(added_products));

  // }
  
  // function addToCart(product_name, product_image, product_price, product_id){

  //   let product = { 'product_id': product_id, 'product_name': product_name, 'product_image': product_image, 'product_price': product_price, 'product_quantity': 1}

  //   console.log('Clicked on Add to Cart', product_name, product_image, product_price)

    // added_products.forEach(element => {
    //   console.log(element.product_id, product_id);
    //   if(element.product_id == product_id){
    //     element.product_quantity += 1;
    //   }
    //   else{
    //     cart_product_number += 1;
    //     total_price += Number(product_price);
    //   }
// 
    // });
    
  //   function removeitem(product_id) {
 
  //     // Declaring a variable to get select element
  //     var a = document.getElementById("list");
  //     var candidate = document.getElementById("candidate");
  //     var item = document.getElementById(candidate.value);
  //     a.removeChild(item);
  // }
    // cart_product_number += 1;
    // total_price += Number(product_price);
    
    // localStorage.setItem('cart_product_number', cart_product_number);
    // localStorage.setItem('total_price', total_price);

    // // pname = `product${cart_product_number}`;
    // // console.log(pname);
    // console.log('added_products keys', Object.keys(added_products));

    // if(Object.keys(added_products).find(element => element == product_id)){

    //   added_products[product_id].product_quantity += 1;
    //   console.log('Added Product Quantity', added_products[product_id], added_products[product_id].product_quantity);

    // }
    // else{
    //   added_products[product_id] = product; 

    // }
    //added_products.push(product) ; 

    
    // localStorage.setItem('added_products', JSON.stringify(added_products));

    // localStorage.setItem('product_image', product_image);
    // localStorage.setItem('product_price', product_price);

  //   basket_num.innerText = cart_product_number;
  //   basket_total_price.innerText = `$${total_price}`;
  //   console.log('added_products', added_products);
  //    alert('products added successfully');
  // }


 

