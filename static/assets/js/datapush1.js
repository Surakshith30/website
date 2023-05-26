var prodName1 = document.querySelector(".product-name").innerHTML;
	console.log(prodName1);
  //query selector for product price
	const parentElement2 = document.querySelector('.price-box');
const prodPrice1 = parentElement2.querySelector('.price').innerHTML;
let newProdPrice1 = prodPrice1.substring(1);
console.log(newProdPrice1);

  var prodId = document.querySelector(".product-id").innerHTML;
	console.log(prodId);

  //query selector for  product category 
const ul1 = document.querySelector('div.breadcrumb-inner');
const secondListItem1 = ul1.querySelectorAll('li')[1];
const clothingValue1 = secondListItem1 .textContent;
console.log(clothingValue1);

function setDataLayerValues1(productName, productPrice, productID, productCategory) {
  // //productName, productPrice, productID , productCategory
  //   productName= document.querySelector("h1.name").innerHTML;
  //   //to get price of the product from product page
  //   const parentElement = document.querySelector('.price-box');
  //   const prodPrice = parentElement.querySelector('.price').innerHTML;
  //   let newProdPrice = prodPrice.substring(1);
  //   // prodPrice.innerHTML =newProdPrice;
  
    // Set data layer variables
    dataLayer.push({
      'event': 'view_item',
      'ecommerce': {
          'item': [{
            'item_name': productName,
            'price': productPrice,
            'item_id' : productID,
            'item_category': productCategory
          }]
        
      }
    });
  }
  
window.onload = setDataLayerValues1(prodName1 ,newProdPrice1, prodId , clothingValue1 );