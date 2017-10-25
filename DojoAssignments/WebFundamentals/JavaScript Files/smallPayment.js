function smallPayment() {
	var penny = 0.01;
	for (var i = 0; i <= 30; i++) {
		penny = penny + penny;
		console.log("Day " + i + ": " + penny);
	}
}

smallPayment();
