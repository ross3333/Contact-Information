document.addEventListener('DOMContentLoaded', function(){
    const countdownElement = document.getElementById('countdown');
  
    let countdownDate = new Date("2024-08-21T23:30:59").getTime();
  
    let x = setInterval(function() {
      let now = new Date().getTime();
      let distance = countdownDate - now;
  
      let days = Math.floor(distance / (1000 * 60 * 60 * 24));
      let hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      let minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
      let seconds = Math.floor((distance % (1000 * 60)) / 1000);
  
      countdownElement.innerHTML = `
        <span>${days} days</span>
        <span>${hours} hours</span>
        <span>${minutes} minutes</span>
        <span>${seconds} seconds</span>
      `;
  
      if (distance < 0) {
        clearInterval(x);
        countdownElement.innerHTML = "EXPIRED";
      }
    }, 1000);
  });