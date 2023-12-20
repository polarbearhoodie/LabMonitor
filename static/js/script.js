function timeString(){
    const date = new Date();

    let year = date.getFullYear();
    let month = date.getMonth();
    let day = date.getDay();
    let hour = date.getHours();
    let minute = date.getMinutes();
    let seconds = date.getSeconds();

    return `${hour}:${minute}:${seconds} - ${month}/${day}/${year}`;
}

function updateCycle(){
    document.getElementById('subheader').innerText = timeString()
}

window.onload = updateCycle;
setInterval(updateCycle, 1000);