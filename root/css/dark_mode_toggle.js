//identify the toggle switch HTML element
const toggleSwitch = document.querySelector(
  '#theme-switch input[type="checkbox"]'
);

//function that changes the theme, and sets a localStorage variable to track the theme between page loads
function switchTheme(e) {
  console.log("Called!");
  console.log(localStorage.getItem("theme"));
  console.log(e.target);
  console.log(e.target.checked);
  if (e.target.checked) {
    localStorage.setItem("theme", "dark");
    document.documentElement.setAttribute("data-theme", "dark");
    toggleSwitch.checked = true;
  } else {
    console.log("");
    localStorage.setItem("theme", "light");
    document.documentElement.setAttribute("data-theme", "light");
    toggleSwitch.checked = false;
  }
  console.log(localStorage.getItem("theme"));
}

//listener for changing themes
toggleSwitch.addEventListener("change", switchTheme, false);

//pre-check the dark-theme checkbox if dark-theme is set
if (document.documentElement.getAttribute("data-theme") == "dark") {
  toggleSwitch.checked = true;
}
