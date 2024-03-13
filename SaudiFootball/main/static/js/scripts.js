let currentClub = 1;
const totalClubs = 4;

function showClub(clubNumber) {
    for (let i = 1; i <= totalClubs; i++) {
        document.getElementById('club' + i).style.display = 'none';
    }
    document.getElementById('club' + clubNumber).style.display = 'block';
}

function showNextClub() {
    currentClub = (currentClub % totalClubs) + 1;
    showClub(currentClub);
}

function showPreviousClub() {
    currentClub = (currentClub - 2 + totalClubs) % totalClubs + 1;
    showClub(currentClub);
}

// Show the initial club
showClub(currentClub);
