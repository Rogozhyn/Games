var difficultyBlock = document.getElementById("choose_difficulty");
var difficultyIndicator = document.getElementById("difficulty_indicator");
var playBody = document.getElementById("play_body");
var display = document.getElementById("userNumberInput");
var gameMessage = document.getElementById("game_message");
var minValueIndicator = document.getElementById("min_value");
var maxValueIndicator = document.getElementById("max_value");
var difficulty
var calculation = "";
var minValue;
var maxValue;
var randomNumber;
var stepsCount;

function chooseDifficulty() {
  let selectedDifficulty = document.querySelector('input[name="difficulty"]:checked');

  if (!selectedDifficulty) {
    alert("Виберіть рівень складності гри.");
    return false;
  }

  difficulty = selectedDifficulty.value;
  minValue = 0;
  if (difficulty === "Легка") {
    maxValue = 10;
  } else if (difficulty === "Середня") {
    maxValue = 100;
  } else {
    maxValue = 1000; //difficulty === "Складна"
  }
  randomNumber = Math.floor(Math.random() * (maxValue - minValue + 1) + minValue);
  console.log(randomNumber);
  stepsCount = 0;

  maxValueIndicator.innerHTML = maxValue
  difficultyIndicator.innerHTML = "Поточна складність гри: " + difficulty;
  gameMessage.innerHTML = "Вкажіть ціле число від " + minValue + " до " + maxValue


  difficultyBlock.style.display = "none"; // Приховати блок
  difficultyIndicator.style.display = "block"; // Показати блок
  playBody.style.display = "block"; // Показати блок

  return false; // Вибір складності не буде відправлений на сервер
}

function appendToDisplay(value) {
    if (display.innerHTML.length == "0" && value == "0" ){
        display.innerHTML = value;
    } else if (display.innerHTML != "0" && parseInt(display.innerHTML + value) <= maxValue){
        calculation = display.innerHTML + value;
        display.innerHTML = calculation;
    }
}

function clearDisplay() {
    display.innerHTML = "";
}

function deleteLast() {
  calculation = display.innerHTML.slice(0, -1); // Видалити останній символ
  display.innerHTML = calculation;
}

function guessNumber() {
    stepsCount += 1;
    var userNumber = parseInt(display.innerHTML);
    console.log(userNumber);

    if (userNumber > randomNumber) {
        gameMessage.innerHTML = "Ваше чило " + userNumber + " більше ніж треба. Спробуйте ще раз."
        display.innerHTML = "";
        maxValue = userNumber-1;
        maxValueIndicator.innerHTML = maxValue;
    }else if (userNumber < randomNumber) {
        gameMessage.innerHTML = "Ваше чило " + userNumber + " менше ніж треба. Спробуйте ще раз."
        display.innerHTML = "";
        minValue = userNumber+1;
        minValueIndicator.innerHTML = minValue;
    } else{
    gameMessage.innerHTML = "Ви вгадали число " + randomNumber + " за " + stepsCount + " спроб! Вітаємо!"
    }
    }