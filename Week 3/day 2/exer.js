// Exercise1

 let nh1=document.querySelector('h1')
    console.log(nh1);

    let hor=document.getElementsByTagName('article')[0].lastElementChild;
      hor.remove()
    console.log(hor);

  // we call the hi tag in order to change the color
  let hore=document.getElementsByTagName('h2')[0];
  hore.addEventListener("click",go);
  function go(){
    hore.style.color="red";
   }

 let dort= document.querySelector("h3");
     dort.addEventListener("click", come)
     function come(){
      dort.style.display="none"
     }

  let fo =document.getElementsByTagName("article")[0]; 
  let rose=document.createElement("button"); 
  rose.innerHTML="click";   
  fo.appendChild(rose);


   let onc=document.querySelectorAll("p")
     rose.addEventListener("click",don)

     function don(){
      for (let i=0; i<=2; i++)
        onc[i].style.fontWeight="bold"
     }





