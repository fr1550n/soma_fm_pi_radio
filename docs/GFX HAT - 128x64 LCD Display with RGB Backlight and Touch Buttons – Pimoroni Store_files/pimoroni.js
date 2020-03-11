

  /* 
    currency localisation 
  */
 var currencies = {}
 currencies.addCurrency = function(iso_code, symbol, locale, rounding) {
   currencies[iso_code] = {iso_code: iso_code, symbol: symbol, locale: locale, rounding: rounding}
 }

currencies.addCurrency("GBP", "&pound;", "en", 0.01)
currencies.addCurrency("BTC", "μɃ", "en", 100.00)
currencies.addCurrency("USD", "$", "en", 0.01)
currencies.addCurrency("EUR", "&euro;", "de", 0.01)
currencies.addCurrency("JPY", "&yen;", "jp", 1.00)
currencies.addCurrency("AUD", "$", "en", 0.01)
currencies.addCurrency("NOK", "kr", "no", 0.01)
currencies.addCurrency("CHF", "CHF", "ch", 0.01)
currencies.addCurrency("NZD", "$", "en", 0.01)
currencies.addCurrency("CAD", "$", "ca", 0.01)

var selectedCurrency = currencies.GBP
if(shop_domain != "shop.pimoroni.com") {
  selectedCurrency = currencies.EUR
}

function selectCurrency(iso_code) {
  if(iso_code in currencies) {
    selectedCurrency = currencies[iso_code]
    Cookies.set("selectedCurrency2", iso_code)
  }else{
    selectedCurrency = currencies.GBP
  }

  updateCurrencies()
}

function updateCartButtons() {
  $(".add-to-cart").each(function(idx, e) {
    var cartButton = $(e)
    cartButton.children("span").remove()

    var variantId = parseInt(cartButton.data("variant-id"))

    if(variantId in cartContents) {
      cartButton.append("<span class='super'>" + cartContents[variantId] + "</span>")
    }
  })
}

function updateCart() {
  $.ajax(
    {
      type: "GET",
      url: "/cart.json",
      dataType: "json",
      success: function(cart) {
        $("#cart_item_count").data("count", cart.item_count)
        $("#cart_item_count").text(cart.item_count)

        total = cart.total_price / 100
        if(shop_domain.indexOf(".com") != -1) {
          taxable_total = 0
          untaxable_total = 0

          for(var item of cart.items) {
            taxable_total += item.taxable ? item.line_price : 0
            untaxable_total += !item.taxable ? item.line_price : 0
          }

          total = (taxable_total * 1.2) + untaxable_total
          total /= 100
        }

        total = total.toFixed(2)
        $("#cart_total").data("total", total)

        value = formatMoney(total)

        cartContents = {}
        for(var item of cart.items) {
          cartContents[item.variant_id] = item.quantity
        }
        updateStockMessages()

        $("#cart_total").html("<span class='super money' gbp='" + total + "'>" + value + "</span>")
        if(shop_domain == "shop.pimoroni.com") {
          updateCurrencies()
        }
        

        updateCartButtons()
      }
    })
}

function formatMoney(gbp) {
  amount = gbp * xchng_rates[selectedCurrency.iso_code]
  prefix = selectedCurrency.symbol
  amount = Math.round(amount / selectedCurrency.rounding) * selectedCurrency.rounding
  return prefix + amount.toLocaleString(selectedCurrency.locale, {minimumFractionDigits: 2, maximumFractionDigits: 2}).replace(/[.,]00$/,"")
}

// called whenever currency values need to be localised (i.e. on page load, or
// when fresh search results are generated)
function updateCurrencies() {
  if(shop_domain == "shop.pimoroni.com") {
    // update the currency picker to show the correct currency    
    console.log(selectedCurrency.iso_code);
    $("#currency_picker a").attr("data-currency", selectedCurrency.iso_code)
    $("#currency_picker a").html("<span></span>" + selectedCurrency.iso_code)

    // determine whether to include VAT in displayed prices
    var hasVAT = ["GBP", "EUR", "BTC"].indexOf(selectedCurrency.iso_code) != -1

    // update each ".money" span
    $(".money").each(function(idx, e) {
      e = $(e)
      if(!e.attr("gbp")) {
        e.attr("gbp", e.text().replace(/[^\d.-]/g, ''))
      }
      gbp = parseFloat(e.attr("gbp"))
      if(!hasVAT) {
        gbp /= 1.2
      }
      e.html(formatMoney(gbp))
    })

    $(".vat").toggle(hasVAT)  // enabled/disable VAT messages

    if(selectedCurrency.iso_code == "GBP") {
      $(".currency-warning").hide();
    }else{
      $(".currency-warning").show();
      $(".currency-warning .currency").text(selectedCurrency.iso_code)
    }
  }
}

$(function() {
  $.fn.isInViewport = function() {
    var o = $(this).offset()	
    var et = o.top
    var eb = et + o.height
    var vt = $(window).scrollTop()
    var vb = vt + $(window).height()
    return eb > vt && et < vb
  };
  
  function loadHires() {
    $("*[data-hires]").each(function(idx, e) {
      if($(this).attr("src")) {
        $(this).attr("src", $(this).data("hires"))        
      }else{
        $(this).css("background-image", "url(" + $(this).data("hires") + ")")
      }      
    })
  }

  
	$(".add-to-cart.ajax").live("click", function(event) {
    var cartButton = $(this)
    cartButton.addClass("processing")

    var variantID = cartButton.data("variant-id")

    $.ajax(
      {
        type:     "POST", url: "/cart/add.js", data: {quantity: 1, id: variantID}, dataType: "json",
        success:  function(data) {
          updateCart()
  
          setTimeout(function() {
            cartButton.removeClass("processing")          

            if(cartButton.hasClass("pre-order")) {
              cartButton.text("Pre-order")
            }else{
              cartButton.text(translations["cart.add_to_cart.submit"])
            }

            cartButton.children("span").remove()
            cartButton.append("<span class='super'>" + data.quantity + "</span>")
          }, 300)            
        },
        error:    function(data) {
          cartButton.removeClass("processing") 
          cartButton.text(translations["cart.add_to_cart.no_more_available"])
          cartButton.addClass("error")
        }
      })
    
		event.preventDefault(); return false;
	});

  function addToCart(variantId, quantity, callback) {
    $.ajax(
      {
        type:     "POST", url: "/cart/add.js", data: {quantity: quantity, id: variantId}, dataType: "json",
        success:  function(data) {callback()},
        error:    function(data) {callback(true)}
      });
  }



  function updateStockMessages() {
    for(variant_id in cartContents) {
      quantity = cartContents[variant_id]
      $("article[data-variant-id='" + variant_id + "'] .stock-message").text(quantity + " " + translations["cart.add_to_cart.in_cart"])
    }
  }
  window.updateStockMessages = updateStockMessages
  updateStockMessages()



  if(shop_domain == "shop.pimoroni.com") {
    // determine if user has selected a preferred currency, if not try to determine
    // their location and choose the most appropriate option.    
    if(Cookies.get("selectedCurrency2")) {
      selectCurrency(Cookies.get("selectedCurrency2"))
    }

    // enable the currency picker the main store
    $("#currency_picker >a")
      .css("display", "inline-block")
      .click(function(e) {
        $("#currencies").css("display", "grid")      
        e.preventDefault()
        return false
    })

    $("#currencies a").click(function(e){    
      $("#currencies").hide()
      selectCurrency($(this).data("currency"))
      e.preventDefault()
      return false
    })
  }


  loadHires()
  
  
  $("#lightbox").click(function(){
    $("#lightbox").hide()
  })

  $("a[data-image]").click(function(e) {
    $("#lightbox img").attr("src", $(this).data("image"))
    $("#lightbox").css("display", "flex")
    e.preventDefault()
    return false
  })
     
  updateCartButtons()
});

updateCart()