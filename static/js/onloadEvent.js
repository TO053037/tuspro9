function onloadEvent() {
	console.log("onload");
	// for (let i = 0; i < 7; i++) {
	// 	getTimeVisitingAllAttractions(i);
	// }

	(async () => {
		const p0 = getTimeVisitingAllAttractions(0);
		const p1 = getTimeVisitingAllAttractions(1);
		const p2 = getTimeVisitingAllAttractions(2);
		await Promise.all([p0, p1, p2]);
	})();


	// onclickDate(0);


}

window.onload = onloadEvent;
