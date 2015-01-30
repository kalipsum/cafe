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

    function previousImage() {

        currentImage = (currentImage + 1) % images.length;
        imageElement.src = images[currentImage];
    }

    var timeoutId = setTimeout(nextImage, 5);
}

