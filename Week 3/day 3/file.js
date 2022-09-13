let newbody=document.getElementsByTagName('body')[0];
let newdiv=document.createElement('div')
let text=document.createTextNode('the banner ends in 10mins')
  newdiv.appendChild(text)
  console.log(newdiv)
  newbody.appendChild(newdiv)
  let dra=newdiv.textContent   
  // textContent is same as inner.HTML 

function sayHi(phrase, who) {
  alert(dra);
}

setTimeout(sayHi, 1000, "Hello", "John"); //  calls sayHi() after one second --> Hello, John