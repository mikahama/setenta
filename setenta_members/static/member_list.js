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
function showDialog(){
	big_black.style.display = "block";
	password_dialog.style.display = "block";
}
function hideDialog(){
	big_black.style.display = "none";
	password_dialog.style.display = "none";
}

function changePassword(){
	var xmlhttp;
	if (window.XMLHttpRequest){
		// code for IE7+, Firefox, Chrome, Opera, Safari
		xmlhttp=new XMLHttpRequest();
	}
	else{
		// code for IE6, IE5
		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  }
	xmlhttp.onreadystatechange=function(){
		if (xmlhttp.readyState==4 && xmlhttp.status==200){
			parsePswrdResponse(xmlhttp.responseText);
		}
	}
	pswrd_error.innerText = "";
	pswrd_success.innerText = "";
	pswrd_button.disabled = true;
	xmlhttp.open("POST","password",true);
	xmlhttp.withCredentials = true ;
	xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	xmlhttp.send("old_password="+old_password.value+"&new_password="+new_password.value+"&csrfmiddlewaretoken="+csrf_token);

}


function parsePswrdResponse(serverResponse){
	var response = JSON.parse(serverResponse);
	pswrd_button.disabled = false;
	pswrd_error.innerText = response.errorMsg;
	pswrd_success.innerText = response.successMsg;
}