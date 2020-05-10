


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