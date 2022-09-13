function name() {
	alert("hello world");
}
setTimeout(name,2000)

function cac(){

	let see=document.getElementById('container')
	let saw=document.createElement('p')
	let myl=document.createTextNode('Hello World')
        see.appendChild(saw)
        saw.appendChild(myl) 
}

let been=setInterval(cac,2000)
function ora(){
	clearInterval(been);
};
 
 function odd(){
    let pic=document.getElementById('container')
	let raw=document.getElementByTagName('p')[0]
	        pic.appendChild(raw)
        raw.appendChild(r) 
      let r= raw.length;

   if(r<5){
   	   odd();

   }else{
   	clearInterval(odd);
   }
};





// for (i=0;i<6;i++){
// 	let sure=setInterval(pod,2000)
// 	function pod(){
// 		cac();
// 	}
// }