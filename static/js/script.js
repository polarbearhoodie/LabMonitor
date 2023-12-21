function prependZero(number){
    return ('0' + number).slice(-2)
}

function timeString(){
    const date = new Date();

    let year = date.getFullYear();
    let month = date.getMonth() + 1;
    let day = date.getDate();
    let hour = date.getHours();
    let minute = prependZero(date.getMinutes());


    if (hour <= 12){
        return `${hour}:${minute}AM - ${month}/${day}/${year}`;
    }
    else{
        return `${hour%12}:${minute}PM - ${month}/${day}/${year}`;
    }
}

function updateCycle(){
    document.getElementById('subheader').innerText = timeString()
}

window.onload = updateCycle;
setInterval(updateCycle, 1000);