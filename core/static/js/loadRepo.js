console.log("loadRepo.js");
let tries = 0;
async function loadRepos() {
  const response = await fetch("/get/repositorios");
  const data = await response.json();
  console.log(data);

  if (data.status === "success") {
    window.location.href = "/";
  } else if (data.status === "unauthorized") {
    window.location.href = "/login";
  } else {
    tries++;
    msg = document.getElementById("msg");
    if (tries < 10) {
        msg.innerHTML = "Retries: " + (tries + 1) + " of 10";
      setTimeout(() => {
        loadRepos();
      }, 1000);
    } else {
        msg.innerHTML = "Network error, please try again later."
        loader = document.getElementById("loader");
        loader.style.display = "none";
    }
  }
}

loadRepos();
