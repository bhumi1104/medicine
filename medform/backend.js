fetch('/api/submitQualityCheck', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(qualityCheckData)
})
.then(response => response.json())
.then(data => {
    alert("Quality check submitted successfully!");
    console.log(data);
})
.catch(error => {
    console.error("Error submitting quality check:", error);
});
