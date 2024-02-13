let register_btn=document.querySelector(".register-btn");
let login_btn=document.querySelector(".login-btn");
let login_nav_btn=document.querySelector(".login-nav-btn");
let close_icon=document.querySelector(".close-icon");
let form_box=document.querySelector(".form-box");
register_btn.addEventListener("click", ()=>{
    form_box.classList.add("change-form");
});
login_btn.addEventListener("click", ()=>{
    form_box.classList.remove("change-form");
});
close_icon.addEventListener("click", ()=>{
    form_box.style.transform="scale(0)";
});
login_nav_btn.addEventListener("click", ()=>{
    form_box.style.transform="scale(1)";
});