function showFlags(){
	var subjectCells = document.getElementsByClassName("table_subjects");
	for (var i = 0; i < subjectCells.length ; i++) {
		var cellText = subjectCells[i].innerText;
		if(cellText.indexOf("\"") > -1 || cellText.indexOf("'") > -1){
			//This is here to block possible code injection
			subjectCells[i].innerText = "";
		}
		else{
			var subjects = subjectCells[i].innerText.split(";");
			var subjectCellHTML = "";
			for (var ii = 0; ii < subjects.length ; ii++) {
				subjectCellHTML = subjectCellHTML + "<img class='table_flag' src='static/flags/"+subjects[ii]+".png'>";
			}
			subjectCells[i].innerHTML = subjectCellHTML;
		}
	}
}