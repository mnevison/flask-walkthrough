document.addEventListener("DOMContentLoaded", function () {
  let sidenav = document.querySelectorAll(".sidenav");
  M.Sidenav.init(sidenav);
});

// Modal

document.addEventListener("DOMContentLoaded", function () {
  let modals = document.querySelectorAll(".modal");
  M.Modal.init(modals, {});
});

// date picker

document.addEventListener("DOMContentLoaded", function () {
  let datepicker = document.querySelectorAll(".datepicker");
  M.Datepicker.init(datepicker, {
    format: "dd mmmm, yyyy",
    i18n: { done: "Select" },
  });
});

// select initilization

document.addEventListener("DOMContentLoaded", function () {
  let selects = document.querySelectorAll("select");
  M.FormSelect.init(selects);
});

// collapsable

document.addEventListener("DOMContentLoaded", function () {
  let collapsibles = document.querySelectorAll(".collapsible");
  M.Collapsible.init(collapsibles);
});
