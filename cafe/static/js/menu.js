var currentImage = 0;
    var images = [
        ('static/images/img2.jpg'),
        ('static/images/img3.jpg'),
        ('static/images/img1.jpg')
    ];
function loadPictures()
{
    var imageElement = document.getElementById('menu_images');

    function nextImage() {

        currentImage = (currentImage + 1) % images.length;
        imageElement.src = images[currentImage];
    }
    var timeoutId = setTimeout(nextImage, 5);
}

function basket_add(item_id){
    var dish = parseInt(document.getElementById("menu-item"+item_id.toString()).value)
    var q = parseInt(document.getElementById("quantity"+item_id.toString()).value)
    if (q>0){$.ajax({
    type: "GET",
    url: "/add/basket",
    data: { item:dish, quantity: q }
    })}
    else{
        alert('quantity should be >0')
    }

return false;
}

function Order(user){
}
