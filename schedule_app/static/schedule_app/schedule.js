let datebtn = document.querySelector('#submit');
    datebtn.addEventListener('click',function(){
    const during = document.getElementById("during").value;

    window.location.href = '/schedule_app/create?during='+during;
    }, false);


let placebtn = document.querySelector('.mj1');
    placebtn.addEventListener('click',function(){
//    const during = document.getElementById("during").value;
//    const place = document.getElementById("1").value;
    window.location.href = '/schedule_app/day';
    }, false);