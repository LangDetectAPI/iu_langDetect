// script.js

document.getElementById("detectButton").addEventListener("click", function() {
    const text = document.getElementById("textInput").value;
    if (text.trim() !== '') { // Vérifie que le texte n'est pas vide.
        detectLanguage(text);
    } else {
        alert("Veuillez entrer du texte.");
    }
});

function detectLanguage(text) {
    const apiKey = 'VOTRE_CLÉ_API'; // Remplacez par votre clé API Google Cloud.
    const url = `https://translation.googleapis.com/language/translate/v2/detect?key=${apiKey}`;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ q: text }),
    })
    .then(response => response.json())
    .then(data => {
        if (data && data.data && data.data.detections) {
            const language = data.data.detections[0][0].language;
            document.getElementById("languageDisplay").textContent = `Langue détectée: ${language}`;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Une erreur s'est produite lors de la détection de la langue.");
    });
}

// resultScript.js

document.getElementById("yesButton").addEventListener("click", function() {
    // Logique à exécuter quand l'utilisateur confirme que la prédiction est correcte
    alert("Vous avez confirmé que la prédiction est correcte.");
    // Ici, vous pourriez par exemple envoyer cette information à un serveur ou enregistrer l'événement.
});

document.getElementById("noButton").addEventListener("click", function() {
    // Logique à exécuter quand l'utilisateur indique que la prédiction n'est pas correcte
    alert("Vous avez indiqué que la prédiction n'est pas correcte.");
    // Ici, vous pourriez par exemple proposer à l'utilisateur de saisir la bonne valeur ou de réessayer.
});

// confirmationScript.js

document.getElementById("resetButton").addEventListener("click", function() {
    // Logique à exécuter pour réinitialiser l'application ou la page
    window.location.reload(); // Ceci recharge la page pour réinitialiser l'état de l'interface.
});
