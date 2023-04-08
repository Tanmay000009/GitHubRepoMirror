let tries = 0;
async function loadOrgRepos() {
  const idDiv = document.getElementById("id");
  const id = idDiv.dataset.id;
  const response = await fetch("/fetch/org/" + id);
  const data = await response.json();

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
        loadOrgRepos();
      }, 1000);
    } else {
        msg.innerHTML = "Network error, please try again later."
        loader = document.getElementById("loader");
        loader.style.display = "none";
    }
  }
}

loadOrgRepos();
