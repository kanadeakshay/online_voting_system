var items = document.querySelectorAll('.element');
// console.log(items);

for (let i = 0; i < items.length; i++) {
    console.log(items[i]);
    link = items[i].querySelector('.vote-btn');
    console.log(link);
    link.addEventListener('click', function () {
        first = items[i].querySelector('.vote');
        console.log(first);
        first.nextElementSibling.classList.toggle('block');
    })
}

const can_vote = document.querySelector('.can_vote');
const message = document.querySelector('.upper');
if (message.textContent == 'There are no elections going on !!') {
    can_vote.classList.add('block');
}
else {
    can_vote.classList.remove('block');
}

// const message02 = document.querySelector('.upper');
// const cand = document.querySelector('.fourth');
// if (message02.textContent == 'Election not started yet') {
//     cand.classList.toggle("see");
// }
