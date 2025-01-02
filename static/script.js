// I'm aware this is goofy
// JavaScript = Cringe

delay = 25;

function sub_live() {
    fetch("/subtract?type=live");
    setTimeout(function () {
        location.reload();
    }, delay);
}
function sub_blank() {
    fetch("/subtract?type=blank");
    setTimeout(function () {
        location.reload();
    }, delay);
}