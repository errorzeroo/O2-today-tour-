let addBtn = document.querySelector('.addBtn');

addBtn.addEventListener('click',function(){
const inputValue = document.getElementById("myInput").value;
}, false);

var slides = document.querySelectorAll('#slides>img');
var prev = document.getElementById('prev');
var next = document.getElementById('next');

var current = 0;

showSlides(current);
prev.onclick = prevSlide ;
next.onclick = nextSlide ;

function showSlides(n) {
    for(var i = 0; i < slides.length; i++) {
        slides[i].getElementsByClassName.display = 'none';
    }
    slides[n].style.display = 'block';
}

// 왼쪽 화살표를 눌렀을때 실행할 함수
function prevSlide(){
    if(current > 0) current -=1;
    else current = slides.length -1;
    showSlides(current)
}

// 오른쪽 화살표를 눌렀을때 실행할 함수
function nextSlide(){
    if(current < slides.length -1) current += 1;
    else current = 0;
    showSlides(current);
}