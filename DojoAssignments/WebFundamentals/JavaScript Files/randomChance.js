var bal = 100;

function randomChance(quarter) {
	console.log('Wanna try your luck?')
	console.log('Your balance is ' + bal);
	for (var i = 0; i < quarter; i++) {
		var luckyNumber = (Math.floor(Math.random() * 101));
		var luckRoll = (Math.floor(Math.random() * 101));
		if (bal < 0) {
			console.log('Not enough coins.');
			break;
		}
		if (luckRoll == luckyNumber) {
			console.log("Jackpot number was " + luckRoll + " , your lucky number was " + luckyNumber);
			console.log('!!!! YOU WIN !!!!');
			bal = bal + Math.floor(Math.random() * 51);
			break;
		} else {
			console.log("Jackpot number was " + luckRoll + " , your lucky number was " + luckyNumber);
			bal--;
			console.log("No luck this time.... :(");
		}
	}
}
