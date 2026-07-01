// Asynchronously update the student's admission status
async function updateStatus() {
  const status = document.getElementById("status-select").value;
  const msgEl = document.getElementById("update-msg");
  const display = document.getElementById("status-display");

  try {
    const res = await fetch(`/update_status/${studentId}`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ status })
    });

    const data = await res.json();

    if (data.success) {
      // Update badge text and class without page reload
      display.textContent = status;
      display.className = `status status-${status.toLowerCase()}`;
      msgEl.textContent = "✓ Status updated successfully.";
      msgEl.style.color = "#0f5132";
    } else {
      msgEl.textContent = data.message || "Update failed.";
      msgEl.style.color = "#c0392b";
    }
  } catch {
    msgEl.textContent = "Network error. Please try again.";
    msgEl.style.color = "#c0392b";
  }
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("update-btn").addEventListener("click", updateStatus);
});
