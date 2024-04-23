function _cloneAnswerBlock() {
    const output = document.querySelector("#api-output");
    const template = document.querySelector('#chat-template');
    const clone = template.cloneNode(true);
    clone.id = "";
    output.appendChild(clone);
    clone.classList.remove("hidden")
    return clone.querySelector(".message");
}

function addToLog(message) {

    const infoBlock = _cloneAnswerBlock();

    infoBlock.innerHTML =  message;
    return infoBlock;
}

function getMessageText() {

    return document.getElementById("prompt").value;
}


async function fetchResponse(prompt) {


    //pause to simulate server response
    await new Promise(r => setTimeout(r, 1000));

    const response = await fetch("/prompt", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body:  JSON.stringify({"text": prompt}),
    });


    return response.body.getReader();
}

async function readResponse(reader, answerBlock) {
    const decoder = new TextDecoder();

    let chunks = "";
    const {done, value} = await reader.read();
    chunks += decoder.decode(value);
    answerBlock.innerHTML = chunks;

}

document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("#prompt-form");
    const spinnerIcon = document.querySelector("#spinner-icon");
    const sendIcon = document.querySelector("#send-icon");

    form.addEventListener("submit", async (event) => {
        event.preventDefault();

        spinnerIcon.classList.remove("hidden");
        sendIcon.classList.add("hidden");

        const prompt = form.elements.prompt.value;

        // Clear the input field
        form.elements.prompt.value = "";

        if (prompt.trim() !== '') {
            addToLog("<b>text</b>: "+prompt);
        }


        try {
            const waitLog = addToLog("Réponse en cours...");
            const reader = await fetchResponse(prompt);
            await readResponse(reader, waitLog);
        } catch (error) {
            console.error('Une erreur est survenue:', error);
        } finally {
            spinnerIcon.classList.add("hidden");
            sendIcon.classList.remove("hidden");


        }
    });
});