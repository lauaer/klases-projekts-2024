//no URL iegūst vārdu
let adrese = window.location.hash;
adrese = decodeURI(adrese);
adrese = adrese.replace('#', '');
adrese = adrese.split(',');
vards = adrese[0];

//mainīgie spēles darbībai
let laiks = 0
let klikski = 0
//masīvi spēles darbībai
const laukumi = ['L01','L02','L03','L04','L05','L06','L07','L08','L09','L10','L11','L12']
const laukumiSaturs = ['👽','🤖','😇','👽','🤕','🤠','🤕','🥶','🤠','🤖','🥶','😇']
let atvertieLaukumi = []
let pedejieDivi =[]

function veiktGajienu(laukums)
{
    console.log('Klikškis uz laukuma '+ laukums)
    klikski++
    let atvertsJaunsLaukums = false
    if (atvertieLaukumi.indexOf(laukums) == -1)
    { atvertsJaunsLaukums = true;
        console.log('atverts jauns laukums')
    }
}