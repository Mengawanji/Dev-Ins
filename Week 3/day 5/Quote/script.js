const quoteText = document.querySelector(".quote");
let quoteBtn = document.querySelector("button");
let authorName = document.querySelector(".name");
let twitterBtn = document.querySelector(".twitter");
let facebookBtn = document.querySelector(".facebook");

// A function to be called when button next quote is clicked
function randomQuote(){
    quoteBtn.classList.add("loading");
    quoteBtn.innerText = "Loading Quote...";
    fetch("https://api.quotable.io/random").then(response => response.json()).then(result => {
        quoteText.innerText = result.content;
        authorName.innerText = result.author;
        quoteBtn.classList.remove("loading");
        quoteBtn.innerText = "New Quote";
    });
}

// Function to redirect user when clicking on twitter button
twitterBtn.addEventListener("click", ()=>{
    let tweetUrl = `https://twitter.com/intent/tweet?url=${quoteText.innerText}`;
    window.open(tweetUrl, "_blank");
});


quoteBtn.addEventListener("click", randomQuote);