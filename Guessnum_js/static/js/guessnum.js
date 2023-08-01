function chooseDifficulty() {
  let selectedDifficulty = document.querySelector('input[name="difficulty"]:checked');

  if (!selectedDifficulty) {
    alert("Виберіть рівень складності гри.");
    return false;
  }

  let difficulty = selectedDifficulty.value;

  let difficultyIndicator = document.getElementById("difficulty_indicator");
  if (difficultyIndicator.style.display === "block") {
    difficultyIndicator.style.display = "none"; // Показати блок
  } else {
    difficultyIndicator.style.display = "block"; // Приховати блок
  }
  difficultyIndicator.innerHTML = "Поточна складність гри: " + difficulty;

    // Отримати посилання на кнопку за допомогою її ідентифікатора
  let playButton = document.getElementById("play");
  // Зробити кнопку неактивною
  playButton.disabled = true;
  // Отримати всі радіо-кнопки за допомогою селектора
  let radioButtons = document.querySelectorAll('input[type="radio"]');
  // Заборонити змінювати стан радіо-кнопок
  radioButtons.forEach((radioButton) => {
    radioButton.disabled = true;
  });

  let chooseDifficulty_ = document.getElementById("choose_difficulty");
  if (chooseDifficulty_.style.display === "block") {
    chooseDifficulty_.style.display = "none"; // Показати блок
  } else {
    chooseDifficulty_.style.display = "block"; // Приховати блок
  }

  return false; // Вибір складності не буде відправлений на сервер
}

function guessNumber(lang) {
  var userNumberInput = document.getElementById("userNumberInput");
  var gameResult = document.getElementById("gameResult");

  console.log('Гра "Вгадайте число" ==>');
  while (true) {
    var difficulty = prompt(
      `Оберіть складність гри:\n1 - Легка\n2 - Середня\n3 - Важка\n>>: `
    );

    console.log("=========================================");
    if (!["1", "2", "3"].includes(difficulty) || difficulty === "") {
      console.log(`Ви вибрали неіснуючий пункт меню. Спробуйте ще раз.`);
      console.log("=========================================");
      continue;
    } else {
      break;
    }
  }

  var min_ = 0;
  var max_ = 0;
  if (difficulty === "1") {
    max_ = 10;
  } else if (difficulty === "2") {
    max_ = 100;
  } else {
    max_ = 1000;
  }

  var number = Math.floor(Math.random() * (max_ - min_ + 1) + min_);
  console.log(number);

  var messages = {
    mes1: {
      ua: `Залишився тільки один варіант ${number}, тому, на жаль, Ви програли.`,
      en: `There is only one variant ${number} left, so, unfortunately, you lost.`,
    },
    mes2: {
      ua: `Вкажіть ціле число від ${min_} до ${max_}: `,
      en: `Enter an integer from ${min_} to ${max_}: `,
    },
    mes3: {
      ua: `Треба вказувати лише цілі числа. Спробуйте ще раз.`,
      en: `Should enter only integers. Try again.`,
    },
    mes4: {
      ua: `Ваше чило {user_number} більше ніж треба. Спробуйте ще раз.`,
      en: `Your number {user_number} is too large. Try again.`,
    },
    mes5: {
      ua: `Ваше чило {user_number} менше ніж треба. Спробуйте ще раз.`,
      en: `Your number {user_number} is less than required. Try again.`,
    },
    mes6: {
      ua: `Ви вгадали число ${number} з першої спроби! Це дуже круто! Вітаємо!`,
      en: `You guessed ${number} on the first try! It's very cool! Congratulations!`,
    },
    mes7: {
      ua: `Ви вгадали число ${number} за {count} спроби! Вітаємо!`,
      en: `You guessed ${number} in {count} tries! Congratulations!`,
    },
    mes8: {
      ua: `Ви вгадали число ${number} за {count} спроб! Вітаємо!`,
      en: `You guessed ${number} in {count} tries! Congratulations!`,
    },
    mes9: {
      ua: "Для завершення натисніть Enter",
      en: "Press Enter to finish",
    },
  };

  var count = 0;
  while (true) {
    var user_number = parseInt(userNumberInput.value, 10);

    if (isNaN(user_number)) {
      console.log(messages.mes3[lang]);
      continue;
    }

    count += 1;
    if (user_number > number) {
      if (user_number - 1 === min_) {
        console.log(messages.mes1[lang]);
        break;
      }
      console.log(messages.mes4[lang]);
      max_ = user_number - 1;
    } else if (user_number < number) {
      if (user_number + 1 === max_) {
        console.log(messages.mes1[lang]);
        break;
      }
      console.log(messages.mes5[lang]);
      min_ = user_number + 1;
    } else {
      if (count === 1) {
        console.log(messages.mes6[lang]);
      } else if (count < 1 || count <= 4) {
        console.log(messages.mes7[lang]);
      } else {
        console.log(messages.mes8[lang]);
      }
      break;
    }
  }

  gameResult.textContent = `${
    "=========================================\n"
  }${messages.mes9[lang]}`;
}