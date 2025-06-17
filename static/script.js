const video = document.getElementById('video');
const resultText = document.getElementById('resultText');
const imagesDiv = document.getElementById('images');

let playerScore = 0;
let computerScore = 0;
let gameOver = false;

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => { video.srcObject = stream; })
    .catch(err => console.error("Webcam error:", err));

function playGame() {
    if (gameOver) return;

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imageData = canvas.toDataURL('image/jpeg');

    fetch('/play', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ image: imageData })
    })
    .then(res => res.json())
    .then(data => {

        // Update scores
        if (data.winner === "Player") {
            playerScore++;
        } else if (data.winner === "Computer") {
            computerScore++;
        }
        // Display current result and scores
        resultText.innerHTML = `
            <p>You: ${data.player} | Computer: ${data.computer} | Winner: ${data.winner}</p>
            <h3>Scores - You: ${playerScore} | Computer: ${computerScore}</h3>
        `;

        // Show images
        imagesDiv.innerHTML = `
            <img src="/static/${data.player}.png" width="100">
            <img src="/static/${data.computer}.png" width="100">
        `;

        // Check if game over
        if (playerScore === 5 || computerScore === 5) {
            gameOver = true;
            const finalWinner = playerScore === 5 ? "🎉 You win the game!" : "💻 Computer wins the game!";
            resultText.innerHTML += `<h2 style="color: green;">${finalWinner}</h2>`;
        }
    })
    .catch(err => console.error('Error:', err));
}

function reset()
{
    playerScore = 0;
    computerScore = 0;
    gameOver = false;
    resultText.innerHTML = "";
    imagesDiv.innerHTML = "";
}