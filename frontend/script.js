document.getElementById("resumeForm").addEventListener("submit", async function(e) {
  e.preventDefault();
  
  let formData = new FormData();
  formData.append("job_description", document.getElementById("job").value);
  formData.append("resume", document.getElementById("resume").files[0]);

  let response = await fetch("/upload", {
    method: "POST",
    body: formData
  });

  let result = await response.json();
  if (result.match_score !== undefined) {
    document.getElementById("result").innerText = `Match Score: ${result.match_score}%`;
  } else {
    document.getElementById("result").innerText = `Error: ${result.error}`;
  }
});
