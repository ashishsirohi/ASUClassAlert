/**
 * Created by ashish on 6/24/17.
 */

function onload(){
    document.getElementById("signup").style.display="none";
    document.getElementById("login").style.display="block";
}

function showLoginForm() {
    document.getElementById("signup").style.display="none";
    document.getElementById("login").style.display="block";
}

function showSignupForm() {
    document.getElementById("signup").style.display="block";
    document.getElementById("login").style.display="none";
}
