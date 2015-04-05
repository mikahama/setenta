function loadOldValues(){
	name.value = old_name.innerText;
	city.value = old_city.innerText;
	var subjects = old_subjects.innerText.split(";");
	for (var i = subjects.length - 1; i >= 0; i--) {
		document.getElementById(subjects[i]).checked = true;
	}
}