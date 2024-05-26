const updateHeaderElement = document.getElementById("update_header");

updateHeaderElement.addEventListener("click", function () {
  const headerElement = document.querySelector("header");

  headerElement.textContent = "New Header!!!";
});