const API = "http://localhost:5000/tasks";

async function loadTasks() {
  const res = await fetch(API);
  const tasks = await res.json();
  const list = document.getElementById("taskList");
  list.innerHTML = "";
  tasks.forEach(t => {
    const li = document.createElement("li");
    li.className = t.status === "complete" ? "complete" : "";
    li.innerHTML = `
      <span>${t.title}${t.due_date ? " (due " + t.due_date + ")" : ""}</span>
      <button onclick="toggleDone(${t.id}, ${t.status !== 'complete'})">
        ${t.status === "complete" ? "Undo" : "Done"}
      </button>
      <button onclick="deleteTask(${t.id})">Delete</button>
    `;
    list.appendChild(li);
  });
}

document.getElementById("addForm").addEventListener("submit", async e => {
  e.preventDefault();
  await fetch(API, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      title: document.getElementById("title").value,
      due_date: document.getElementById("due").value
    })
  });
  e.target.reset();
  loadTasks();
});

async function toggleDone(id, makeComplete) {
  await fetch(`${API}/${id}`, {
    method: "PUT",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({status: makeComplete ? "complete" : "pending"})
  });
  loadTasks();
}

async function deleteTask(id) {
  await fetch(`${API}/${id}`, {method: "DELETE"});
  loadTasks();
}

loadTasks();   // initial load