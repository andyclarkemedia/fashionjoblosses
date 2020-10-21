// ===========================
// Helper Functions 
// ===========================


// DOM STUFF
const submitButton = document.querySelector('#submit-search-button')
const searchBar = document.querySelector("#search-box-input")
const responseContainer = document.querySelector("#response-container")
const productName = document.querySelector('#product-name')
const heading = document.querySelector('#heading')
const responseDescription = document.querySelector('#response-description')
const dietaryRequirementsSelectForm = document.querySelector("#dietary-preferences")
let options = document.getElementsByTagName('option')



// Helper function to make requests 
const url = "https://world.openfoodfacts.org/api/v0/product/"

const getFromApi = function(barcodeInput, funcToCall, jsonObj) {
	const queryUrl = url + barcodeInput + ".json" //+encodeURI(jsonObj)
	axios.get(queryUrl)
	.then(function(res) {
		funcToCall(res)
	})
}

submitButton.addEventListener("click", function() {
	// VALUES ARRAY 
	let values = []
	let requirements = []

	Object.keys(options).forEach(function(item) {
		requirements.push(options[item].value)
		
		if (options[item].selected) {
			values.push(1)
		} else {
			values.push(0)
		}
	})

	//console.log(values)
	//console.log(requirements)
	var result = {};
	requirements.forEach((key, i) => result[key] = values[i]);
	console.log(result)
	// Declare barcode value
	const barcode = searchBar.value

	// Call Function to API
	getFromApi(barcode, renderResponse, result)
})

// DISPLAY RESULTS 

const renderResponse = function(responseObject) {
	console.log(responseObject)
	// IF PRODUCT NOT FOUND
	if (responseObject.status === 0) {
		alert("Sorry! We couldn't find a product match.\n\nPlease try again !");
	} 
	// IF PRODUCT FOUND
	else {
		// Display response content
		responseContainer.style.display = "grid";
		// Create resopnse product name
		productName.innerHTML = "Can I eat ... "  //+ responseObject.name
		// Create image tag 
		const image = document.createElement('img')
		// CHECK FOR RED, GREEN, YELLOW
		// Img class
		image.className = "trafficLight"
		// Green 
		if (responseObject.status === 200) {
			// Set SRC
			image.src = "https://svgur.com/i/HXk.svg"
			heading.innerHTML = "All Clear"
			responseDescription.innerHTML = "You can eat this!"
		} 
		// YELLOW
		else if (responseObject.status === 204) {
			image.src = "https://svgur.com/i/HXt.svg"
			heading.innerHTML = "Hmmm ... Probably Not"
			responseDescription.innerHTML = "We not sure, check the ingredients below\n"
			const ingredients = document.createElement("p");
			ingredients.innerHTML = "" // responseObject.ingredients.maybe
		}
		 // RED
		else {
			image.src = "https://svgur.com/i/HZW.svg"
			heading.innerHTML = "Don't Go There!"
			responseDescription.innerHTML = "You cannot eat this!"
		}
		responseContainer.appendChild(image) 
	}
}



// Create 

