player_name = prompt("enter your name");
alert("Hello " + player_name);
player_guess = prompt("Rock, Paper or Scissors?");
computer_guess = randomInteger(1, 3);
if (player_guess == computer_guess) {
  document.getElementById("user_feedback").innerHTML =
    "<em>Correct, You WIN</em>";
} else {
  document.getElementById("user_feedback").innerHTML =
    "Incorrect, you LOSE, dummy\n" + "The computer guessed " + computer_guess;
}

function randomInteger(min, max) {
  return Math.floor(Math.random() * (max - min + 1) + min);
}
