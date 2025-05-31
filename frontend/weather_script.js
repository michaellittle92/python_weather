async function create_weather_element() {
  let weather_element = document.createElement("div");

  let image = document.createElement("img");
  image.src = "https://placehold.co/600x400";

  let day = document.createElement("label");
  let max_temp = document.createElement("label");
  let min_temp = document.createElement("label");

  let max_temp_content = document.createTextNode("max_temp");
  let min_temp_content = document.createTextNode("min_temp");
  let day_content = document.createTextNode("day");

  day.appendChild(day_content);
  max_temp.appendChild(max_temp_content);
  min_temp.appendChild(min_temp_content);

  weather_element.appendChild(image);
  weather_element.appendChild(day);
  weather_element.appendChild(max_temp);
  weather_element.appendChild(min_temp);

  container.appendChild(weather_element);
}

async function getData() {
  const url = "http://127.0.0.1:8000/weather_data";

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error(`response status: ${response.status}`);
    }

    const json = await response.json();
    console.log(json);
  } catch (error) {
    console.error(error.message);
  }
}

async function main() {
  let container = document.getElementById("container");
  for (let i = 0; i < 10; i++) {
    create_weather_element();
  }
}

main();
getData();
