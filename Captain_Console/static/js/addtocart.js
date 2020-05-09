


function addToCart(productId,userId) {
  // const id = $(elem).attr('id');
  $.ajax({
    url:            "/cart/addto",
    type:           'POST',
    beforeSend:     function (request) {
      request.setRequestHeader("X-CSRFToken", crfToken);
    },
    data: {
        'productId': productId,
        'userId': userId
    },
    contentType:    'application/json; charset=utf-8',
    dataType:       'json',
    success:  function (result) {
      console.log("Allt fór vel")
      console.log(result)
    }
  });
}