const projectCardsGroup = document.getElementById("project-cards-group")

async function getRepos() {
    try {
        const response = await fetch("/api/github");

        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }

        const result = await response.json();
        result.forEach((repo) => {
            let cardElement = document.createElement("div");
            const repoName = titleCase(repo.name);
            if (repo.description) {
                repoDesc = repo.description;
            }
            else {
                repoDesc = "Keine Beschreibung vorhanden";
            }
            cardElement.innerHTML = `<div class="project-card"><div class="project-card-container"><h4>${repoName}</h4><p>${repoDesc}</p><hr><p><a href="${repo.html_url}" target="_blank" rel="noopener noreferrer"><b>Link zum Repository</b></a></p></div></div>`;
            projectCardsGroup.appendChild(cardElement);
        });
    }
    catch (error) {
        console.error(error.message);
    }
}

document.addEventListener("DOMContentLoaded", () => {
    if (projectCardsGroup) {
        getRepos();
    }
});


function titleCase(str) {

    if (!str) {
        return "";
    }

    let capitalizedRepoName = "";

    str.split("_").forEach(word => {
        const capitalizedWord = word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
        capitalizedRepoName += capitalizedWord + " ";
    });

    return capitalizedRepoName;
}
