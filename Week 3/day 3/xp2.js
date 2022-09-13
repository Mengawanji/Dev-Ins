    function myMove() {
    	let box=  document.getElementById('animate')
    	let displacement=0;
    	let int= setInterval(() =>{
    		if(displacement<350){
    			displacement++;
    			box.style.left=displacement+"px"
    		}else{
    			clearInterval(int)
    		}
    	}, 5)
    }