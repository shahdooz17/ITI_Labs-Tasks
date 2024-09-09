document.getElementById('change-text-btn').addEventListener('click', function() {
    document.getElementById('main-title').textContent = 'Hello, JavaScript!';
});

document.getElementById('change-html-btn').addEventListener('click', function() {
    document.getElementById('description').innerHTML = '<strong>This HTML has been changed!</strong>';
});
