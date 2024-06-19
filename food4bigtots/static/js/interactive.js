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
