let datebtn = document.querySelector('#datebtn');

    datebtn.addEventListener('click',function(){
    const startdate_in = document.getElementById("startdate").value;
    const enddate_in = document.getElementById("enddate").value;
    console.log(enddate_in)
    window.location.href = '/schedule_app/createdate?startdate='+startdate_in+'&enddate='+enddate_in;
    }, false);