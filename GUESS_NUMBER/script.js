let randomNumber = Math.floor(Math.random() * 100) + 1;
let attemptsLeft = 5;

function checkGuess() {
    let userGuess = parsetInt(document.getElementById('guess' . value));
    let message = document.getElementById('message');
    let tries = document.getElementById('tries');

    if (isNaN(userGuess) || userGuess < 1 || userGuess > 100) {
        message.innerText = "Please enter a number between 1 and 100!";
        return;
    }

    attemptsLeft--;

    if (userGuess === randomNumber) {
        message.innerText = "Congratulations! You guessed the number!";
        message.style.color = "green";
        tries.innerText = "Game Over!"; disableInput();
    } else if (attemptsLeft === 0) {
        message.innerText = `You lost! The number was ${randomNumber}. `;
        message.style.color = "red";
        tries.innerText = "No tries left!.";
        disableInput();
    }else if (userGuess < randomNumber)
{
    message.innerText = "too low! Try again.";
    } else {
        message.innerText = "Too high! Try again.";
    }

    tries.innerText = `Tries Left: $ {attemptsLeft}`;
}

function disableInput() {

document.getElementById('guess').disable = true;

document.querySelector("button").disable = true;
}