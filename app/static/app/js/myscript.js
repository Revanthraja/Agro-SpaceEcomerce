$('.plus-cart').click(function(){
    var id=$(this).attr('pid').toString();

    var enl=(this.parentNode.children[2]);
    console.log("pid=",id)

    $.ajax({
        type:"GET",
        url:"/pluscart",
        data:{
            prod_id:id
        },
success:function(data){
    console.log("data=",data);
    enl.innerText=data.quantity
    document.getElementById("amount").innerText=data.amount 
    document.getElementById("totalamount").innerText=data.totalamount
    
}



})

})

$('.minus-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this.parentNode.children[2] 
    $.ajax({
        type:"GET",
        url:"/minuscart",
        data:{
            prod_id:id
        },
        success:function(data){
            eml.innerText=data.quantity 
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
        }
    })
})

$('.remove-cart').click(function(){
    var id=$(this).attr("pid").toString();
    var eml=this
    $.ajax({
        type:"GET",
        url:"/removecart",
        data:{
            prod_id:id
        },
        success:function(data){
            document.getElementById("amount").innerText=data.amount 
            document.getElementById("totalamount").innerText=data.totalamount
            eml.parentNode.parentNode.parentNode.parentNode.remove() 
        }
    })
})

$('.plus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/pluswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            var encodedId = encodeURIComponent(id);
            var redirectUrl = `http://127.0.0.1:8000/product-detail/${encodedId}`;
            window.location.href = redirectUrl;
        }
    });
});

$('.minus-wishlist').click(function() {
    var id = $(this).attr("pid").toString();
    $.ajax({
        type: "GET",
        url: "/minuswishlist",
        data: {
            prod_id: id
        },
        success: function(data) {
            var encodedId = encodeURIComponent(id);
            var redirectUrl = `http://127.0.0.1:8000/product-detail/${encodedId}`;
            window.location.href = redirectUrl;
        }
    });
});
