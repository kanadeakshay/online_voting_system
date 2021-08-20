const inputs = document.querySelectorAll(".input");


function addcl() {
    let parent = this.parentNode.parentNode;
    parent.classList.add("focus");
}

function remcl() {
    let parent = this.parentNode.parentNode;
    if (this.value == "") {
        parent.classList.remove("focus");
    }
}


inputs.forEach(input => {
    input.addEventListener("focus", addcl);
    input.addEventListener("blur", remcl);
});

const voter_form = document.querySelector('.voter-form');
const admin_form = document.querySelector('.admin-form');
const admin_link = document.querySelector('.admin-link');
const back_btn = document.querySelector('.back');

admin_link.addEventListener('click', () => {
    voter_form.style.display = 'none';
    admin_form.style.display = 'block';
});

back_btn.addEventListener('click', () => {
    voter_form.style.display = 'block';
    admin_form.style.display = 'none';
});