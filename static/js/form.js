// Fetch data.json and populate select boxes asynchronously
async function populateSelects() {
  const response = await fetch("/static/data/data.json");
  const data = await response.json();

  fillSelect("department", data.departments);
  fillSelect("level", data.levels);
  fillSelect("region", data.regions);
}

// Helper: populate a <select> element with an array of options
function fillSelect(id, options) {
  const select = document.getElementById(id);
  select.innerHTML = `<option value="">-- Select --</option>`;
  options.forEach(opt => {
    const el = document.createElement("option");
    el.value = opt;
    el.textContent = opt;
    select.appendChild(el);
  });
}

// Client-side validation before form submission
function validateForm(e) {
  const form = document.getElementById("portal-form");
  const inputs = form.querySelectorAll("input[required], select[required]");
  const genderChecked = form.querySelector("input[name='gender']:checked");

  for (const input of inputs) {
    if (!input.value.trim()) {
      alert(`Please fill in: ${input.id || input.name}`);
      input.focus();
      e.preventDefault();
      return;
    }
  }

  if (!genderChecked) {
    alert("Please select a gender.");
    e.preventDefault();
  }
}

document.addEventListener("DOMContentLoaded", () => {
  populateSelects();
  document.getElementById("portal-form").addEventListener("submit", validateForm);
});
