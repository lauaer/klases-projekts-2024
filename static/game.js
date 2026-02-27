//no URL iegūst vārdu
let adrese = window.location.hash.substring(1);
let vards = decodeURI(adrese.split(',')[0] || '').trim();

//mainīgie spēles darbībai
let laiks = 0;
let klikski = 0;

//taimera mainīgie, taimeris strādā ar 1.klikski
let timerId = null;
let timerStarted = false;

function formatTime(seconds) {
    const m = String(Math.floor(seconds / 60)).padStart(2, '0');
    const s = String(seconds % 60).padStart(2, '0');
    return `${m}:${s}`
}

function updateHUD() {
    const elLaiks = document.querySelector('#laiks');
    const elKlikski = document.querySelector('#klikski');
    if (elLaiks) elLaiks.textContent = formatTime(laiks);
    if (elKlikski) elKlikski.textContent = klikski;
}

function startTimerIfNeeded() {
    if (timerStarted) return;
    timerStarted = true;
    timerId = setInterval(() => {
        laiks++;
        updateHUD();
    }, 1000);
}

function stopTimer() {
    if (timerId) {
        clearInterval(timerId);
        timerId = null;
    }
}

//masīvi spēles darbībai
const laukumi = ['L01','L02','L03','L04','L05','L06','L07','L08','L09','L10','L11','L12']
const laukumiSaturs = ['👽','🤖','😇','👽','🤕','🤠','🤕','🥶','🤠','🤖','🥶','😇']
let atvertieLaukumi = []
let pedejieDivi = []

//Sajauc smailikus nejaušā secībā (Fisher-Yates algoritms)
let laukumiSajaukti = [...laukumiSaturs].sort(() => Math.random() - 0.5);



//Ģenerē spēles laukumu dinamiski
document.addEventListener("DOMContentLoaded", function() {
    //ja vāds nav, aizūta uz sākumlapu
    if (!vards) {
        window.location.href = '/';
        return;
    }

    let spelesLauks = document.querySelector('.speles_lauk');
    spelesLauks.innerHTML = '';
    laukumiSajaukti.forEach((emoji, index) => {
        let bloks = document.createElement("div");
        bloks.classList.add("bloks");
        bloks.setAttribute("data-index", index);
        bloks.innerText = "";
        bloks.addEventListener("click", function() {
            veiktGajienu(bloks, emoji);
        });
        spelesLauks.appendChild(bloks);
    });

    const elVards = document.querySelector('#vardsHUD');
    if (elVards) elVards.textContent = vards;
    updateHUD();
});

function veiktGajienu(bloks, emoji) {
    if (bloks.classList.contains("atverts") || pedejieDivi.length === 2) {
        return //neļauj klikšķināt uz jau atvērtām kartītēm vai ja 2 atvērtas
    }
    
    startTimerIfNeeded();
    //parāda emoji tikai uzklikšķinot
    bloks.innerText = emoji;
    bloks.classList.add("atverts");
    klikski++;
    updateHUD();

    //saglabā 2 pēdējās kartītes
    pedejieDivi.push({bloks, emoji});

    //ja atvērtas 2 kartītes, pārbauda vai sakrīt
    if (pedejieDivi.length === 2) {
        let [pirmais, otrais] = pedejieDivi;
        //ja atvērtas 2 kartītes, pārbauda vai vienādas
        if (pirmais.emoji === otrais.emoji) {
            atvertieLaukumi.push(pirmais, otrais);
            pedejieDivi = [];

            //vai spēle pabeigta (visi laukumi atvērti)
            if (atvertieLaukumi.length === laukumiSajaukti.length) {
                stopTimer();

                //parāda rezultātu
                setTimeout(() => {
                    alert(`Apsveicu, ${vards}!\nKlikski: ${klikski}\nLaiks: ${formatTime(laiks)}`);
                    //vardu un rezultatu nodod uz top sadaļu caur URL
                    document.location = `/tops#${encodeURIComponent(vards)},${klikski},${laiks}`;
                }, 300);

            }
        } else {
            //ja 2 atvērtie nav vienādi
            setTimeout(() => {
                pirmais.bloks.innerText = "";
                otrais.bloks.innerText = "";
                pirmais.bloks.classList.remove("atverts");
                otrais.bloks.classList.remove("atverts");
                pedejieDivi = [];
            }, 800);
        }
    }
}