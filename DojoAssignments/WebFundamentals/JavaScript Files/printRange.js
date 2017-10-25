function printRange(startPoint, endPoint, skipAmt) {
	if (skipAmt == null) {
		skipAmt = 1;
	}
	for (var i = startPoint; i < endPoint; i += skipAmt) {
		console.log(i);
	}
}

printRange(-2, 10, 2);