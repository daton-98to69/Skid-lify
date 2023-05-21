var myButton = document.getElementById("myButton");
var ongoingEvents = document.getElementById("ongoing_events");

myButton.addEventListener("click", function () {
  if (ongoingEvents.classList.contains("hidden")) {
    ongoingEvents.classList.remove("hidden");
    ongoingEvents.style.bottom = "0";
    myButton.style.bottom = "40vh";
  } else {
    ongoingEvents.style.bottom = "-40vh";
    ongoingEvents.addEventListener(
      "transitionend",
      function () {
        ongoingEvents.classList.add("hidden");
      },
      { once: true }
    );
    myButton.style.bottom = "10px";
  }
});

document.addEventListener("click", function (event) {
  if (
    !myButton.contains(event.target) &&
    !ongoingEvents.contains(event.target)
  ) {
    ongoingEvents.style.bottom = "-40vh";
    ongoingEvents.addEventListener(
      "transitionend",
      function () {
        ongoingEvents.classList.add("hidden");
      },
      { once: true }
    );
    myButton.style.bottom = "10px";
  }
});
