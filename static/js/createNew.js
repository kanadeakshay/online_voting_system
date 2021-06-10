const add_candidates_btn = document.querySelector('.add-candidates-btn');
const popup = document.querySelector('.popup');
const close_popup = document.querySelector('.close-popup');

add_candidates_btn.addEventListener('click', () => {
    popup.style.visibility = 'visible';
});

close_popup.addEventListener('click', () => {
    popup.style.visibility = 'hidden';
});