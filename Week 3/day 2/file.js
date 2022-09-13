 function insertRow() {
 	let box =document.getElementById('sampleTable')

 	let newtr= document.createElement('tr')
 	let newtd= document.createElement('td')
 	let text= document.createTextNode('cell4')

 	newtd.appendChild(text)
 	newtr.appendChild(newtd)
 	box.appendChild(newtr)
 	console.log(box); 
 }
   let btn = document.getElementById('new')
   console.log(btn)
   btn.addEventlistener('click',change style)

   function changeStyle(){
   	  btn.style.color="blue"
 }