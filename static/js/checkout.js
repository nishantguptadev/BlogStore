
    if (localStorage.getItem("cart") == null) {
	  var cart = { };
	} else {
        cart = JSON.parse(localStorage.getItem("cart"));
	}
    console.log(cart);
    var sum = 0;
    var totalPrice = 0;
    if ($.isEmptyObject(cart)) {
        // If cart is empty
        mystr =
        "<p>Your cart is empty, please add some items before checking out ! </p>";
    $("#items").append(mystr);
	} else {
  
	for (item in cart) {

        let name = cart[item][1];
    let qty = cart[item][0];
    let itemPrice = cart[item][2];
    sum = sum + qty;
    itemtotal= qty*itemPrice;
    totalPrice= totalPrice + qty*itemPrice;

	 // mystr = `<ul class="list-group">
	//	  <li class="list-group-item d-flex justify-content-between align-items-center">
	//		  ${name}
	//		<span class="badge bg-primary rounded-pill">${qty}</span><br>
	//	  </li></ul>`

    mystr = `<tr>
        <th class="table-success" scope="row">${name}</th>
        <td class="table-success">${itemPrice}</td>
        <td class="table-success">X ${qty}</td>
        <td class="table-success">${itemtotal}</td>
    </tr>`;

    $("#items").append(mystr);

	}
  }

    document.getElementById("cart").innerHTML = sum;
    document.getElementById("totalPrice").innerHTML = totalPrice;
    document.getElementById("sum").innerHTML = sum;
    $("#itemsJson").val(JSON.stringify(cart)); //store items in database

    $('#amount').val ($('#totalPrice').html())

