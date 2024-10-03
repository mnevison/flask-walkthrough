document.addEventListener("DOMContentLoaded", function () {
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
});

// Modal

document.addEventListener("DOMContentLoaded", function () {
  let modals = document.querySelectorAll(".modal");
  M.Modal.init(modals, {});
});
