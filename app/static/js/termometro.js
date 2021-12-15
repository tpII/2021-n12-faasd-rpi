const units = {
	Celcius: "°C",
	Fahrenheit: "°F"
};

const config = {
	min: 0,
	maxTemp: 50,
	maxHum: 100,
	unit: "Celcius"
};

// 
const temperature = document.getElementById("temperature");
const humidity = document.getElementById("humidity");

function setearTemperatura(numero){
    temperature.style.height = (numero - config.min) / (config.maxTemp - config.min) * 100 + "%";
	temperature.dataset.value = numero + units[config.unit];
}

function setearHumedad(numero){
    humidity.style.height = (numero - config.min) / (config.maxHum - config.min) * 100 + "%";
	humidity.dataset.value = numero + "%";
}