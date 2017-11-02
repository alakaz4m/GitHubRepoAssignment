var day = 365
function smallPayment() {
	var penny = 0.01;
	for (var i = 1; i <= day; i++) {
		penny = penny + penny;
		console.log("Day " + i + ": " + penny);
	}
}

smallPayment();
