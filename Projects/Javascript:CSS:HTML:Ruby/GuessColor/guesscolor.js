var colorsString = "blue,cyan,gold,gray,green,magenta,orange,red,white,yellow";
var colorsArray = colorsString.split(",")
var target;
var guess_input_text;
var guess_input;
var finished = false;
var guesses = 0;

function do_game(){
	var random_number = Math.random()*colorsArray.length;
	var random_number_integer = Math.floor(random_number)+1;
	target = colorsArray[random_number_integer]

	while(!finished){
		guess_input_text = prompt("I am thinking of one of these colors \n\n " + 
									 colorsString + "\n\n"  +
									"What color am I thinking of?");
		
		guesses +=1;
		finished = check_guess();
		
	}

}

function check_guess(){
	if(typeof(guess_input_text) != typeof("a beautiful string")){
		alert("That is not a string! You crazy!");
		return false;
	}
	if(typeof(guess_input_text) == typeof("a beautiful string") && colorsArray.indexOf(guess_input_text) == -1 ){
		alert("Sorry that color wasn't in my list!");
		return false;
	}
	if(guess_input_text > target){
		alert("Sorry, your guess is not correct! \n\n"
			+ "Hint: your color is alphabetically higher than mine. \n\n" +
			"Please try again.");
		return false;
	}
	if(guess_input_text < target){
		alert("Sorry, your guess is not correct! \n\n"
			+ "Hint: your color is alphabetically lower than mine. \n\n" +
			"Please try again.");
		return false;
	}
	alert("You got it! The color was " + target +
			". \n\nIt took you " + guesses + 
			" guesses to get the number!");
	myBody=document.getElementsByTagName("body")[0];


	myBody.style.background=target;
		return true;
}






