// TODO: Toggle list state, AJAX.

// Remember to always wait for the DOM to be fully loaded.
// Event handlers can only take callbacks (no calls!).
// 'this' cannot be used. Events must be passed into callbacks.
$(document).ready(function(){
    $('.card').hover(function(event){
        toggleDisplay(event);
    }, function(event){
        toggleDisplay(event);
    });
});

function toggleDisplay(event){
    // Remember to select the event using $()!
    // Know the difference between event.Target and event.currentTarget.
    // Credit for the solution goes to ChatGPT: https://chatgpt.com/share/67146b64-2b00-800c-9a9d-7fa7e4a4a578.
    let target = $(event.currentTarget);
    target.children(".card-img").toggleClass("d-none");
    target.children(".card-body").toggleClass("d-flex");
    target.children(".card-body").toggleClass("d-none");
}

function displayText(event){
    let target = $(event.currentTarget);
    target.children(".card-img").addClass("d-none");
    target.children(".card-body").removeClass("d-none");
    target.children(".card-body").addClass("d-flex");
}

function displayImage(event){
    let target = $(event.currentTarget);
    target.children(".card-img").removeClass("d-none");
    target.children(".card-body").removeClass("d-flex");
    target.children(".card-body").addClass("d-none");
}
