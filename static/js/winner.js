// if winner_name.textContent == 'none' :
//     hide everything except heading and winner_votes
// heading.textcontext = 'there was a draw since x parties got equal votes' and dispaly winner_votes
// else :
// show everything

const winner_name = document.querySelector('#winner_name');
const winner_votes = document.querySelector('#winner_votes');
const winner_party = document.querySelector('#winner_party');
const winner_id = document.querySelector('#winner_id');

const name1 = document.querySelector('#name');
const votes = document.querySelector('#votes');
const party = document.querySelector('#party');
const id = document.querySelector('#id');

if (name1.textContent == 'none') {
    winner_party.style.display = 'none';
    winner_id.style.display = 'none';
    name1.innerHTML = 'There was a draw since some candidates got equal votes';
}