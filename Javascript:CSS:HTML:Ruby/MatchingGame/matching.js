var numberOfFaces = 5;
var theLeftSide = document.getElementById("leftSide");
var theRightSide = document.getElementById("rightSide");
var theBody = document.getElementsByTagName("body")[0];// grab the first body tag? not sure why we are indexing


function generateFaces(){
	for(i = 0; i < numberOfFaces; i++){
		var smiley = document.createElement("img");
		smiley.src = "smile.png";
		var rando = Math.floor(Math.random()*400+1);// random number between 0 and 400
		smiley.style.top = rando.toString() + "px";
		var rando2 = Math.floor(Math.random()*400+1);// random number between 0 and 400
		smiley.style.left = rando2.toString() + "px";
		theLeftSide.appendChild(smiley);
	}
	console.log("There are " + numberOfFaces + " smileys");
	var leftSideImages = theLeftSide.cloneNode(true); // copy the nodes from left side
	leftSideImages.removeChild(leftSideImages.lastChild); //remove last node
	theRightSide.appendChild(leftSideImages); //add copy to right side

	//eventhandler to last face on left side (correct choice)

	theLeftSide.lastChild.onclick = function nextLevel(event){
			event.stopPropagation(); // ensures event does not apply to other elements

			numberOfFaces += 5;

			//delete child nodes 

			var myNode = document.getElementById("leftSide");
			while (myNode.firstChild) {
		    	myNode.removeChild(myNode.firstChild);
			}

			var myNode = document.getElementById("rightSide");
			while (myNode.firstChild) {
			    myNode.removeChild(myNode.firstChild);
			}

			generateFaces();

		};

	//eventhandler for making an incorrect decision

	theBody.onclick = function gameOver(){
			alert("Game Over!");

			theBody.onclick = null; //prevents anything from happening when clicking body

			theLeftSide.lastChild.onclick = null; // prevents anything from happening when clicking last face

			if(confirm("Want to play again?")){
				location.reload();

			};

		};

	
}
