console.log('Hello World!');

volume = 0
fuel = 0

function burn() {
  fuel += 6000
}

setInterval(function() {
  if (fuel > 0 && volume < 6000) {
    fuel -= 100
    volume += 5
  } else {
    fuel = 0
  }
  document.getElementById("volume").value = volume
  document.getElementById("fuel").innerHTML = `${Math.round(volume/60)} ${fuel == 0 ? "" : "+" + (Math.floor(fuel/1000) <= -1 ? 0 : Math.round(fuel/1000))}`
  
}, 1000/60)
