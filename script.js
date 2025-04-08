document.getElementById('send-btn').onclick = async function() {
    const input = document.getElementById('user-input');
    const messages = document.getElementById('messages');

    const userText = input.value;
    messages.innerHTML += `<div><strong>You:</strong> ${userText}</div>`;

    const response = await fetch('http://localhost:8000/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: userText})
    });

    const data = await response.json();
    messages.innerHTML += `<div><strong>LLM:</strong> ${data.reply}</div>`;

    input.value = '';
    messages.scrollTop = messages.scrollHeight;
};
