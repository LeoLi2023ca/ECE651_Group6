let register_btn = document.querySelector(".Register-btn");
let login_btn = document.querySelector(".Login-btn");
let form = document.querySelector(".Form-box");
register_btn.addEventListener("click", ()=>{
    form.classList.add("change-form");
});
login_btn.addEventListener("click", ()=>{
    form.classList.remove("change-form");
});
