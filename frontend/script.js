document.addEventListener('DOMContentLoaded', () => {
    const messagesArea = document.getElementById('chat-messages');
    const userInput = document.getElementById('user-input');
    const sendBtn = document.getElementById('send-btn');
    const sessionId = 'session-' + Math.random().toString(36).substr(2, 9);

    function addMessage(content, role) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${role}`;

        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        bubble.textContent = content;

        messageDiv.appendChild(bubble);
        messagesArea.appendChild(messageDiv);

        // Scroll to bottom
        messagesArea.scrollTop = messagesArea.scrollHeight;
        return messageDiv;
    }

    const loginModal = document.getElementById('login-modal');
    const loginForm = document.getElementById('login-form');
    const chatContainer = document.querySelector('.chat-container');
    const firstNameInput = document.getElementById('first-name');
    const lastNameInput = document.getElementById('last-name');
    const emailInput = document.getElementById('email');

    let userData = null;

    // Handle Login Form
    loginForm.addEventListener('submit', (e) => {
        e.preventDefault();

        userData = {
            firstName: firstNameInput.value.trim(),
            lastName: lastNameInput.value.trim(),
            email: emailInput.value.trim()
        };

        // Cache user data (optional)
        localStorage.setItem('chat_user', JSON.stringify(userData));

        // Hide modal and unblur chat
        loginModal.classList.add('hidden');
        chatContainer.classList.remove('blurred');
        userInput.focus();
    });

    // For development, we'll let the user see the login every time as requested
    // localStorage.getItem('chat_user') bypass removed

    async function sendMessage() {
        const text = userInput.value.trim();
        if (!text || !userData) return;

        // Clear input and disable
        userInput.value = '';
        userInput.disabled = true;
        sendBtn.disabled = true;

        // Add user message to UI
        addMessage(text, 'user');

        // Add typing indicator
        const typingIndicator = document.createElement('div');
        typingIndicator.id = 'typing';
        typingIndicator.className = 'typing-indicator';
        typingIndicator.textContent = 'Assistant is typing...';
        messagesArea.appendChild(typingIndicator);
        messagesArea.scrollTop = messagesArea.scrollHeight;

        try {
            // Explicitly using 127.0.0.1:8000 to avoid DNS/localhost issues
            const response = await fetch('http://127.0.0.1:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    message: text,
                    first_name: userData.firstName,
                    last_name: userData.lastName,
                    email: userData.email
                }),
            });

            const data = await response.json();

            // Remove typing indicator
            const indicator = document.getElementById('typing');
            if (indicator) indicator.remove();

            if (response.ok) {
                addMessage(data.response, 'assistant');
            } else {
                // Show server-side detail if it exists
                const errorMsg = data.detail || 'Something went wrong on the server.';
                addMessage(errorMsg, 'error');
            }
        } catch (error) {
            console.error('Error:', error);
            const indicator = document.getElementById('typing');
            if (indicator) indicator.remove();
            addMessage('Network error. Is the backend running? Make sure to run python run.py', 'error');
        } finally {
            userInput.disabled = false;
            sendBtn.disabled = false;
            userInput.focus();
        }
    }

    sendBtn.addEventListener('click', sendMessage);

    userInput.addEventListener('keypress', (e) => {
        if (e.key === 'Enter') {
            sendMessage();
        }
    });

    userInput.focus();
});
