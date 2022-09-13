    let me=document.getElementsByClassName('square')[0]
    let you=document.getElementsByClassName("grid-container")[0]
    you.appendChild(me)
    for(let i=0; i<=1440;i++){
    	let div=document.createElement('div')  
        me.appendChild(div) 
        div.setAttribute('class','right')
        div.style.border="2px solid black"
    
 }

