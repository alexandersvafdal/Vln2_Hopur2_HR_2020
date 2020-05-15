function back() {
  window.history.back();
}


function addToCart(productId) {
  $.ajax({
    url:            "/cart/addto",
    type:           'POST',
    beforeSend:     function (request) {
      request.setRequestHeader("X-CSRFToken", crfToken);
    },
    data: {
        'productId': productId
    },
    contentType:    'application/json; charset=utf-8',
    dataType:       'json',
    success:  function (result) {

    }
  });
}

function addedToCart(){
  const elem = document.getElementById('addedToCartDiv');
  elem.classList.toggle('d-none');
  elem.style.opacity = 1;
  (function fade(){(elem.style.opacity-=.1)<0?elem.classList.toggle('d-none'):setTimeout(fade,250)})();
}

function deletedFromCart(){
  const elem = document.getElementById('deletedFromCart');
  elem.classList.toggle('d-none');
  elem.style.opacity = 1;
  (function fade(){(elem.style.opacity-=.1)<0?elem.classList.toggle('d-none'):setTimeout(fade,250)})();
}

function addedToCartHome(){
  const elem = document.getElementById('addedToCartDivHome');
  elem.classList.toggle('d-none');
  elem.style.opacity = 1;
  (function fade(){(elem.style.opacity-=.1)<0?elem.classList.toggle('d-none'):setTimeout(fade,250)})();
}

function deleteFromCart(productId) {

  $.ajax({
    url:            "/cart/delete",
    type:           'DELETE',
    beforeSend:     function (request) {
      request.setRequestHeader("X-CSRFToken", crfToken);
    },
    data: {
        'productId': productId
    },
    contentType:    'application/json; charset=utf-8',
    dataType:       'json',
    success:  function (result) {
      location.reload()
    }
  });
}