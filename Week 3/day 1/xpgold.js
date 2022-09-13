let x = document.querySelectorAll("tr");
console.log(x)

      for (let i=1; i<=x.length; i++){
            let dor=document.querySelector(`tr:nth-of-type(${i}) td:nth-of-type(${i})`);
            dor.style.backgroundColor ='red';
             console.log(dor);
    }
